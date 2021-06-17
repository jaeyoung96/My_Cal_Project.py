import numpy as np
import math
import cv2


### Camera coordinate to vehicle coordinate(ISO)
def RotX(Pitch):  # Pitch = 14
    Pitch = np.deg2rad(Pitch)  # degree 함수 radian 함수로 변환
    return [[1, 0, 0], [0, math.cos(Pitch), -math.sin(Pitch)], [0, math.sin(Pitch), math.cos(Pitch)]]


def RotY(Yaw):  # Yaw = 0
    Yaw = np.deg2rad(Yaw)
    return [[math.cos(Yaw), 0, math.sin(Yaw)], [0, 1, 0], [-math.sin(Yaw), 0, math.cos(Yaw)]]


def RotZ(Roll):  # Roll = 0
    Roll = np.deg2rad(Roll)
    return [[math.cos(Roll), -math.sin(Roll), 0], [math.sin(Roll), math.cos(Roll), 0], [0, 0, 1]]


### Camera parameter setting
ImageSize = (480, 640)
FocalLength = (309.4362, 344.2161)  # 렌즈 중심과 이미지 센서와의 거리
PrinciplePoint = (318.9034, 257.5352)  # 이미지 평면의 주요 지점
IntrinsicMatrix = ((FocalLength[0], 0, 0), (0, FocalLength[1], 0), (PrinciplePoint[0], PrinciplePoint[1], 1))
# IntrinsicMatrix = ((309.4362, 0, 0), (0, 344.2161, 0), (318.9034, 257.5352, 1))
Height = 2.1798  # 카메라 높이 : 2.18m
Pitch = 14  # 카메라 지면에서 14도 피치로 배치
Yaw = 0
Roll = 0

### Bird's eye view setting
DistAhead = 30
SpaceToOneSide = 6
BottomOffset = 3.0

OutView = (BottomOffset, DistAhead, -SpaceToOneSide, SpaceToOneSide)  # (3.0, 30, -6, 6)
OutImageSize = [math.nan, 250]
WorldHW = (abs(OutView[1] - OutView[0]), abs(OutView[3] - OutView[2]))  # (27, 12)

Scale = (OutImageSize[1] - 1) / WorldHW[1]  # 249 / 12 = 20.75
ScaleXY = (Scale, Scale)  # (20.75, 20.75)

OutDimFrac = Scale * WorldHW[0]  # 20.75 * 27 = 560.25
OutDim = round(OutDimFrac) + 1  # 560.25 반올림, 560+1 = 561
OutImageSize[0] = OutDim  # OutImageSize = (561, 250)

### Homography Matrix Compute

# Translation Vector
Rotation = np.matmul(np.matmul(RotZ(-Yaw), RotX(90 - Pitch)), RotZ(Roll))
# (RotZ(-Yaw) * RotX(90-Pitch)) * RotZ(Roll), [[1,0,0],[0,0.24,-0.97],[0,0.97,0.24]]
TranslationinWorldUnits = (0, 0, Height)  # (0,0,2.18)
Translation = [np.matmul(TranslationinWorldUnits, Rotation)]  # [0, 2.12, 0.53]

# Rotation Matrix
RotationMatrix = np.matmul(RotY(180),
                           np.matmul(RotZ(-90), np.matmul(RotZ(-Yaw), np.matmul(RotX(90 - Pitch), RotZ(Roll)))))
# [[-6.12323400e-17 -2.41921896e-01  9.70295726e-01]
#  [-1.00000000e+00  1.48134438e-17 -5.94134778e-17]
#  [-7.49879891e-33 -9.70295726e-01 -2.41921896e-01]]
# Camera Matrix
CameraMatrix = np.matmul(np.r_[RotationMatrix, Translation], IntrinsicMatrix)
# [[ 3.09430606e+02  1.66611893e+02  9.70295726e-01]
#  [-3.09436200e+02 -1.02020360e-14 -5.94134778e-17]
#  [-7.71497150e+01 -3.96294815e+02 -2.41921896e-01]
#  [ 1.68170949e+02  8.63843437e+02  5.27341348e-01]]
CameraMatrix2D = np.r_[[CameraMatrix[0]], [CameraMatrix[1]], [CameraMatrix[3]]]
# list 합치기, CameraMatrix2D = CameraMatrix[0, 1, 3]
# Compute Vehicle-to-Image Projective Transform
VehicleHomo = np.linalg.inv(CameraMatrix2D)  # CameraMatrix2D 역행렬

AdjTransform = ((0, -1, 0), (-1, 0, 0), (0, 0, 1))
BevTransform = np.matmul(VehicleHomo, AdjTransform)  # 입력 이미지, bird-eye_image로 변경
DyDxVehicle = (OutView[3], OutView[1])  # (6, 30)
tXY = [a * b for a, b in zip(ScaleXY, DyDxVehicle)]  # (20.75*6, 20.75*30) = [124.5, 622.5]
# test = np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
ViewMatrix = ((ScaleXY[0], 0, 0), (0, ScaleXY[1], 0), (tXY[0] + 1, tXY[1] + 1, 1))
# ((20.75, 0, 0), (0, 20.75, 0), (125.5, 623.5, 1))
T_Bev = np.matmul(BevTransform, ViewMatrix)
# [[ 6.70574419e-02  4.10608408e-18  1.05529828e-35]
#  [ 1.62293085e-01  8.20876249e-01  1.29317199e-03]
#  [-4.92525955e+01 -1.62339935e+02 -2.22053780e-01]]
T_Bev = np.transpose(T_Bev)  # 행과 열 바꾸기
# [[ 6.70574419e-02  1.62293085e-01 -4.92525955e+01]
#  [ 4.10608408e-18  8.20876249e-01 -1.62339935e+02]
#  [ 1.05529828e-35  1.29317199e-03 -2.22053780e-01]]

### Main
src = cv2.imread("testImage.png", cv2.IMREAD_COLOR)
# 원근 변환 함수, 원근 맵 행렬에 대한 기하학적 변환
BirdEyeView = cv2.warpPerspective(src, T_Bev, (OutImageSize[1], OutImageSize[0]))
# (src, matrix, width = 250, height = 561)
'''cv2.imshow("BEV", BirdEyeView)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

### Distance

# Vehicle to Image
'''toOriginalImage = np.linalg.inv(np.transpose(T_Bev))
Trans = np.linalg.inv(np.matmul(toOriginalImage, VehicleHomo))
VehiclePoint = [[20, 0]]
XV = np.r_[VehiclePoint[0], np.shape(VehiclePoint)[0]]
UV = np.matmul(XV, Trans)

UV[0:2] = UV[0:2]/UV[2]
ImagePointsimport numpy as np
import math
import cv2


### Camera coordinate to vehicle coordinate(ISO)
def RotX(Pitch):  #     Pitch = 14
      Pitch = np.deg2rad(Pitch)     # degree 함수 radian 함수로 변환
      return [[1, 0, 0], [0, math.cos(Pitch), -math.sin(Pitch)], [0, math.sin(Pitch), math.cos(Pitch)]]

def RotY(Yaw):    # Yaw = 0
      Yaw = np.deg2rad(Yaw)
      return [[math.cos(Yaw), 0, math.sin(Yaw)], [0, 1, 0], [-math.sin(Yaw), 0, math.cos(Yaw)]]

def RotZ(Roll):   # Roll = 0
      Roll = np.deg2rad(Roll)
      return [[math.cos(Roll), -math.sin(Roll), 0], [math.sin(Roll), math.cos(Roll), 0], [0, 0, 1]]      
### Camera parameter setting
ImageSize = (480, 640)
FocalLength = (309.4362, 344.2161)  # 렌즈 중심과 이미지 센서와의 거리
PrinciplePoint = (318.9034, 257.5352)     # 이미지 평면의 주요 지점
IntrinsicMatrix = ((FocalLength[0], 0, 0), (0, FocalLength[1], 0), (PrinciplePoint[0], PrinciplePoint[1], 1))
# IntrinsicMatrix = ((309.4362, 0, 0), (0, 344.2161, 0), (318.9034, 257.5352, 1))
Height = 2.1798   # 카메라 높이 : 2.18m
Pitch = 14        # 카메라 지면에서 14도 피치로 배치
Yaw = 0
Roll = 0

### Bird's eye view setting
DistAhead = 30
SpaceToOneSide = 6
BottomOffset = 3.0

OutView = (BottomOffset, DistAhead, -SpaceToOneSide, SpaceToOneSide) # (3.0, 30, -6, 6)
OutImageSize = [math.nan, 250]
WorldHW = (abs(OutView[1]-OutView[0]), abs(OutView[3]-OutView[2]))      # (27, 12)

Scale = (OutImageSize[1]-1)/WorldHW[1]    # 249 / 12 = 20.75
ScaleXY = (Scale, Scale)      # (20.75, 20.75)

OutDimFrac = Scale*WorldHW[0] # 20.75 * 27 = 560.25
OutDim = round(OutDimFrac)+1  # 560.25 반올림, 560+1 = 561
OutImageSize[0] = OutDim      # OutImageSize = (561, 250)

### Homography Matrix Compute

#Translation Vector
Rotation = np.matmul(np.matmul(RotZ(-Yaw),RotX(90-Pitch)),RotZ(Roll))
# (RotZ(-Yaw) * RotX(90-Pitch)) * RotZ(Roll), [[1,0,0],[0,0.24,-0.97],[0,0.97,0.24]]
TranslationinWorldUnits = (0, 0, Height)  # (0,0,2.18)
Translation = [np.matmul(TranslationinWorldUnits, Rotation)] # [0, 2.12, 0.53]

#Rotation Matrix
RotationMatrix = np.matmul(RotY(180), np.matmul(RotZ(-90), np.matmul(RotZ(-Yaw), np.matmul(RotX(90-Pitch), RotZ(Roll)))))
# [[-6.12323400e-17 -2.41921896e-01  9.70295726e-01]
#  [-1.00000000e+00  1.48134438e-17 -5.94134778e-17]
#  [-7.49879891e-33 -9.70295726e-01 -2.41921896e-01]]
#Camera Matrix
CameraMatrix = np.matmul(np.r_[RotationMatrix, Translation], IntrinsicMatrix)
# [[ 3.09430606e+02  1.66611893e+02  9.70295726e-01]
#  [-3.09436200e+02 -1.02020360e-14 -5.94134778e-17]
#  [-7.71497150e+01 -3.96294815e+02 -2.41921896e-01]
#  [ 1.68170949e+02  8.63843437e+02  5.27341348e-01]]
CameraMatrix2D = np.r_[[CameraMatrix[0]], [CameraMatrix[1]], [CameraMatrix[3]]]
# list 합치기, CameraMatrix2D = CameraMatrix[0, 1, 3]
#Compute Vehicle-to-Image Projective Transform
VehicleHomo = np.linalg.inv(CameraMatrix2D)     # CameraMatrix2D 역행렬

AdjTransform = ((0, -1, 0), (-1, 0, 0), (0, 0, 1))
BevTransform = np.matmul(VehicleHomo, AdjTransform)   # 입력 이미지, bird-eye_image로 변경
DyDxVehicle = (OutView[3], OutView[1])     # (6, 30)
tXY = [a*b for a,b in zip(ScaleXY, DyDxVehicle)] # (20.75*6, 20.75*30) = [124.5, 622.5]
#test = np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
ViewMatrix = ((ScaleXY[0], 0, 0), (0, ScaleXY[1], 0), (tXY[0]+1, tXY[1]+1, 1))
# ((20.75, 0, 0), (0, 20.75, 0), (125.5, 623.5, 1))
T_Bev = np.matmul(BevTransform, ViewMatrix)
# [[ 6.70574419e-02  4.10608408e-18  1.05529828e-35]
#  [ 1.62293085e-01  8.20876249e-01  1.29317199e-03]
#  [-4.92525955e+01 -1.62339935e+02 -2.22053780e-01]]
T_Bev = np.transpose(T_Bev)   # 행과 열 바꾸기
# [[ 6.70574419e-02  1.62293085e-01 -4.92525955e+01]
#  [ 4.10608408e-18  8.20876249e-01 -1.62339935e+02]
#  [ 1.05529828e-35  1.29317199e-03 -2.22053780e-01]]

### Main
src = cv2.imread("testImage.png", cv2.IMREAD_COLOR)
# 원근 변환 함수, 원근 맵 행렬에 대한 기하학적 변환
BirdEyeView = cv2.warpPerspective(src, T_Bev, (OutImageSize[1], OutImageSize[0]))
# (src, matrix, width = 250, height = 561)
'''cv2.imshow("BEV", BirdEyeView)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
 

### Distance

#Vehicle to Image
'''toOriginalImage = np.linalg.inv(np.transpose(T_Bev))
Trans = np.linalg.inv(np.matmul(toOriginalImage, VehicleHomo))
VehiclePoint = [[20, 0]]
XV = np.r_[VehiclePoint[0], np.shape(VehiclePoint)[0]]
UV = np.matmul(XV, Trans)

UV[0:2] = UV[0:2]/UV[2]
ImagePoints = list(map(int, UV[0:2]))

print(ImagePoints)
annotatedBEV1 = cv2.drawMarker(BirdEyeView, ImagePoints, (0,0,255))
cv2.putText(annotatedBEV1, "20 meters", ImagePoints, cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0))

cv2.imshow("BEV", annotatedBEV1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Image to Vehicle
toOriginalImage = np.linalg.inv(np.transpose(T_Bev))  # T_Bev 행,열 바꾼 값 역행렬
Trans = np.matmul(toOriginalImage, VehicleHomo)
# T_Bev 행,열 바꾼 값의 역행렬 * CameraMatrix2D 역행렬
ImagePoint = [[120, 400]]

UI = ImagePoint
UI = np.r_[ImagePoint[0], np.shape(ImagePoint)[0]]    # [120 400   1]
XI = np.matmul(UI, Trans)     # [10.77108434  0.26506024  1.        ]
XI[0:2] = XI[0:2]/XI[2] # XI의 [0, 1] XI[2] 로 각각 나눠주기
XAhead = XI[0]    # XI[0]

# annotatedBEV2 = cv2.drawMarker(BirdEyeView, ImagePoint[0], (0,0,255))
# cv2.putText(annotatedBEV2, str(round(XAhead, 2))+" meters", ImagePoint[0], cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0))
annotatedBEV2 = cv2.drawMarker(BirdEyeView, tuple(ImagePoint[0]), (0,0,255))
cv2.putText(annotatedBEV2, str(round(XAhead, 2))+" meters", tuple(ImagePoint[0]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0))

cv2.imshow("BEV", annotatedBEV2)
cv2.waitKey(0)
cv2.destroyAllWindows() = list(map(int, UV[0:2]))

print(ImagePoints)
annotatedBEV1 = cv2.drawMarker(BirdEyeView, ImagePoints, (0,0,255))
cv2.putText(annotatedBEV1, "20 meters", ImagePoints, cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0))

cv2.imshow("BEV", annotatedBEV1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

# Image to Vehicle
toOriginalImage = np.linalg.inv(np.transpose(T_Bev))  # T_Bev 행,열 바꾼 값 역행렬
Trans = np.matmul(toOriginalImage, VehicleHomo)
# T_Bev 행,열 바꾼 값의 역행렬 * CameraMatrix2D 역행렬
ImagePoint = [[120, 400]]

UI = ImagePoint
UI = np.r_[ImagePoint[0], np.shape(ImagePoint)[0]]  # [120 400   1]
XI = np.matmul(UI, Trans)  # [10.77108434  0.26506024  1.        ]
XI[0:2] = XI[0:2] / XI[2]  # XI의 [0, 1] XI[2] 로 각각 나눠주기
XAhead = XI[0]  # XI[0]

# annotatedBEV2 = cv2.drawMarker(BirdEyeView, ImagePoint[0], (0,0,255))
# cv2.putText(annotatedBEV2, str(round(XAhead, 2))+" meters", ImagePoint[0], cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0))
annotatedBEV2 = cv2.drawMarker(BirdEyeView, tuple(ImagePoint[0]), (0, 0, 255))
cv2.putText(annotatedBEV2, str(round(XAhead, 2)) + " meters", tuple(ImagePoint[0]), cv2.FONT_HERSHEY_DUPLEX, 0.5,
            (0, 255, 0))

cv2.imshow("BEV", annotatedBEV2)
cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import pandas as pd

mydf = pd.DataFrame(np.random.randint(1,100,(6,4)), columns = list('ABCD'))
print(mydf)
# 6일치 Datatime64 데이터형 인덱스 생성
mydf.index = pd.date_range('20170701',periods=6)
print(mydf.index)
print(mydf)

mydf['E'] = [23,52,np.NAN,90,np.NAN,75]
print(mydf)
print(mydf['E'].notnull())  # 'E' column 불러와서 null값이 아니면 True
print(mydf.iloc[0:2,1:3])   # 행,열 숫자 사용한 Data Slicing

mydf.iloc[0,0] = np.NAN
mydf.iloc[3,2] = np.NAN
print(mydf)
# 컬럼 기준으로 결측 데이터가 하나라도 포함된 행 추출
print(mydf[mydf.isnull().any(axis=1)])  # axis : column
print(mydf)
# del mydf['E']
# print(mydf)
# delcol = ['A','C','E']
# for col in delcol:
#     del mydf[col]
# print(mydf)
# 날짜 데이터 datetime형으로 변경, inplace:원본 변경 허용
mydf.drop(pd.to_datetime('20170704'), inplace=False)
print(mydf)
print(mydf.index)
dfindex = pd.to_datetime('2017-08-01')
print(dfindex,type(dfindex))    # Timestamp형태의 data로 변환
print(mydf.drop([pd.to_datetime('20170704'), pd.to_datetime('20170705')],inplace=False))

mydf.drop(['B','D'],axis=1,inplace=True)
print(mydf)

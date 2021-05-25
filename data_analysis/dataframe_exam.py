import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#mydf = pd.DataFrame({'A':[1,2,3], 'B':[5,6,7]})    # 전달인자 넘어가면 객체 원하는 값으로 초기화
#mydf = pd.DataFrame([[1,2,3],[5,6,7]])    # 전달인자 넘어가면 객체 원하는 값으로 초기화

arr = np.arange(0,15).reshape(5,3)
print(arr)
print(arr.shape)    # n행,n열 행렬
print(arr.ndim)     # n차원

mydf = pd.DataFrame(arr,columns=list('ABC'))
print(mydf)
mydf.index = pd.date_range('20210401', periods=5, freq='d')
# index:20210401 부터 5만큼의 day 증가, ex)freq=4d(4일),7h(7시간),3m(3달)
print(mydf)
print(mydf.loc['20210402':'20210404'])  # 슬라이싱 해서 출력
# print(mydf)
# print(mydf.index) # index list로 정렬해서 출력
# print(mydf.index[0])
# mydf.index[0] = 'four'  # index는 수정 불가능
# 같은 이름의 index 여러개 설정 가능
# reindex : 새로운 객체 생성 후 index 재배열
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

mydf.dropna(how='any', inplace=False)  # 행 기준 하나라도 NaN 있으면 삭제
print(mydf)

mydf.dropna(subset=['E'],axis=0,inplace=False)   # 특정 column 기준으로 NaN이 하나라도 있는 index 삭제
print(mydf)
mydf.loc[pd.to_datetime('20180308')] = np.NAN   # index에 2018-03-08 추가
print(mydf)
mydf.dropna(how='all', inplace=True)    # column이 모두 NaN값일 경우에 삭제
print(mydf)

mydf.fillna(value=99.9, inplace=False)
print(mydf)  # 결측치에 NaN 대신 value 값 대입
import numpy as np
import pandas as pd

mydf = pd.read_csv('score.csv',index_col=0, encoding='CP949') # 어떠한 열을 index로 잡을것인가 설정
print(mydf)
# mydf.fillna(value=99,inplace=True)
# print(mydf)
mydf.loc['토탈'] = [mydf['철수'].sum(), mydf['영희'].sum(), mydf['길동'].sum()]
mydf['점수 합계'] = [mydf.loc['국어'].sum(), mydf.loc['수학'].sum(), mydf.loc['영어'].sum(),np.NAN]
print(mydf)
mydf.dropna(how='any', inplace=True)  # 행 기준 하나라도 NaN 있으면 삭제
print(mydf)

mydf.to_csv('score1.csv', encoding='CP949')   # 데이터 프레임 객체에 내용을 CSV 파일로 저장
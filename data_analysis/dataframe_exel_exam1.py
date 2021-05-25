import numpy as np
import pandas as pd

peopledf = pd.read_excel('population_in_seoul.xls')
print(peopledf)

peopledf.drop(0,inplace=True)
print(peopledf)
peopledf['도시'] = '서울'
print(peopledf)
peopledf.loc[peopledf['자치구'] == '금천구','도시'] = '경기'
print(peopledf)
peopledf = peopledf.append({'자치구':'임시구','남자':2000,'여자':3000,'고령자':4000,'도시':'서울'},ignore_index=True)
print(peopledf)
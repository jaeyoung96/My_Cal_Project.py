import numpy as np
import pandas as pd

arr = np.random.randint(-10,10,(5,))
print(arr)
sr = pd.Series(arr)
data = sr[sr > 0]    # Fancy 색인
print(data)

dict_data = { 'customer' : ['kim','park','Lee'],
				'pay' : [5000,6000,7000],
				'local' : ['seoul','pusan','jeju'],
				'card' : ['9440','4805','4602'] }

df = pd.DataFrame(dict_data, index=['one','two','three'])
print(df)
# print(df.info()) # df의 정보 출력
# print(df.describe)

df1 = pd.DataFrame(np.random.randint(10,size=(3,3)), index=['01','02','03'],
                   columns = list('ABC'))   # columns : 가로 열을 list 안의 문자들로 대체
print(df1)

df1.rename(columns={'A':'K'},inplace=True)  # 행열의 요소 다른 이름으로 대체
print(df1)
df1.rename(index={'01':'08'},inplace=True)
print(df1)

df1['D'] = [3,5,6]  # 'D'라는 column 추가
print(df1)

print('K col sum:',df1['K'].sum())
print('B col sum:',df1['B'].sum())
print('C col sum:',df1['C'].sum())

df1.loc['total'] = np.NAN
df1['total'] = np.NAN
df1.loc['total','K'] = df1['K'].sum()   # total, K 에 K열의 sum값 대입
print(df1)

df1 = df1.loc['02':'02','K':'B']    # 데이터의 원하는 행열값만 slicing
print(df1)
df1.loc['04'] = np.NAN  # '04'라는 행 추가
print(df1)
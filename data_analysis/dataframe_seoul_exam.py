import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

peopledf = pd.read_excel('population_in_seoul.xls')
peopledf.drop(0,inplace=True)
print(peopledf)

columns = ['남자', '여자', '고령자']
for x in columns:
    print(peopledf.loc[peopledf[x].isnull()])
    print('='*50)

peopledf.dropna(how = 'any', inplace = True)
print(peopledf)
del peopledf['고령자']
print(peopledf)
peopledf.reset_index(drop=True,inplace=True)    # index 재 정리
print(peopledf)

peopledf.plot(kind='bar')
plt.show()

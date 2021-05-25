import numpy as np
import pandas as pd
arr1 = np.random.randint(1,45,size=(6,))
print(arr1)
mydf = pd.DataFrame({'A':[1,2,3],'B':[3,6,9], 'C':np.array([12,15,18])})
print(mydf)
print(mydf['A'])
print(mydf['C'])
print(mydf.loc[1:, 'A':'B'])


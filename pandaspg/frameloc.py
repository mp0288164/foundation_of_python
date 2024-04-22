#modify and add columns with help of loc function
import pandas as pd
dict={'a':[2,3,4,5,6],'b':[21,43,65,87,98],'c':[123,455,686,778,908],'d':[1000,2000,3000,4000,5000]}
print(dict)
mks1=pd.DataFrame(dict)
print(mks1)
mks1.loc[:,'e']=[5,8,1,6,7]
print(mks1)
mks1.loc[2,:]=[1,2,3,4,5]
print(mks1)
mks1.loc[5,:]=[10,21,13,14,51]
print(mks1)
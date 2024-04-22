import pandas as pd
dict={'a':[2,3,4,5,6],'b':[21,43,65,87,98],'c':[123,455,686,778,908],'d':[1000,2000,3000,4000,5000]}
print(dict)
mks1=pd.DataFrame(dict)
print(mks1)
mks2=pd.DataFrame(mks1,copy=True)
mks2.b[2]=56
print(mks2)
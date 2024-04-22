#head and tail function in pandas in frame
import pandas as pd
dict={"a":[2,34,56,78,90],"b":[12,23,43,54,56],"c":[122,43,76,87,90]}
mks1=pd.DataFrame(dict)
print(mks1)
print(mks1.head())#head() by default displaying starting five rows
print(mks1.tail())#tail() by default displaying five row bottom of frame
print(mks1.head(3))#head(n)displaying n=1,2,3,4,5,6..... top of the frame
print(mks1.tail(3))#tail(n)displaying n=1,2,3,4,5,6..... bottom of the frame


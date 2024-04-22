import pandas as pd
dict={"a":[2,34,56,78,90],"b":[12,23,43,54,56],"c":[122,43,76,87,90]}
mks1=pd.DataFrame(dict)
print(mks1)
mks1=pd.DataFrame(dict,index=["A","B","C","D","E"])
print(mks1)
print(mks1.cummax()) #find maximum no in coloum and replace it
print(mks1.cummin())#find minimum no in coloum and replace it
print(mks1.cummax(axis=1))#find maximum in row and replace it
print(mks1.cummin(axis=1))#find minimum in row and replace it
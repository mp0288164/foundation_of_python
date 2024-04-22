#cuminity sum ,cumsum
import pandas as pd
dict={"a":[2,34,56,78,90],"b":[12,23,43,54,56],"c":[122,43,76,87,90]}
mks1=pd.DataFrame(dict)
print(mks1)
mks1=pd.DataFrame(dict,index=["A","B","C","D","E"])
print(mks1)
print(mks1.cumsum())
#cumsum() work like 1,2,3,4,5. {1,1+2=3,3+3=6,6+4=9,9+5=14,resulted(1,3,6,9,14)}
print(mks1.cumsum(axis=1))
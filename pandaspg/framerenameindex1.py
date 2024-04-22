#renaming a row
import pandas as pd
dict={"a":[9,8,7,6,4],"b":[7.8,9.0,5.6,7.6,8.8],"d":[11,43,67,89,90]}
mks1=pd.DataFrame(dict,index=['I','II','III','VI','V'])
print(mks1)
mks1.rename(index={'I':1,'II':2,'III':3,'VI':4,'V':5},inplace=True)
print(mks1)

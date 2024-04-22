import pandas as pd
# max() function in pandas
dict1={"a":{"I":23,"II":21,"III":54,"VI":12,"V":43},"b":{"I":90,"II":98,"III":54,"VI":72,"V":13},"c":{"I":30,"II":20,"III":50,"VI":22,"V":40}}
def1=pd.DataFrame(dict1)
print(def1)
print(def1.max())#default find maximum column wise
print(def1.max(axis=1,skipna=True,numeric_only=True))#find maximum row wise
print(def1.iloc[:,0:1].max())
print(def1.iloc[0:2,:].max(axis=1))

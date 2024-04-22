import pandas as pd
dict1={"a":{"I":23,"II":21,"III":54,"VI":12,"V":43},"b":{"I":90,"II":98,"III":54,"VI":72,"V":13},"c":{"I":30,"II":20,"III":50,"VI":22,"V":40}}
def1=pd.DataFrame(dict1)
print(def1)
print(def1.min())
print(def1.min(axis=1))
print(def1.iloc[:,0:1].min())
print(def1.iloc[1:3,:].min())
print(def1.iloc[:,0:1].min(axis=1,skipna=True,numeric_only=True))
print(def1.iloc[1:3,:].min(axis=1,skipna=True,numeric_only=True))
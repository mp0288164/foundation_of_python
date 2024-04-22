import pandas as pd
#min() function in pandas
dict1={"a":{"I":23,"II":21,"III":54,"VI":12,"V":43},"b":{"I":90,"II":98,"III":54,"VI":72,"V":13},"c":{"I":30,"II":20,"III":50,"VI":22,"V":40}}
dict2={"a":{"I":34,"II":71,"III":94,"VI":32,"V":63},"b":{"I":50,"II":48,"III":24,"VI":92,"V":43},"c":{"I":31,"II":22,"III":54,"VI":82,"V":49}}
def1=pd.DataFrame(dict1)
print(def1)
def2=pd.DataFrame(dict2)
print(def1.min())#default find minimum column wise
print(def1.min(axis=1,skipna=True,numeric_only=True))#axis=1 means find minimum row wise
print(def1.loc[:,"a":"b"].min())# find specified minimum column wise [ :,column]
print(def1.loc["I":"II",:].min(axis=1))#find specified minimum roe wise[row,:]

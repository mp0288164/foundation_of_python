import pandas as pd
#binary operation
dict1={"a":{"I":23,"II":21,"III":54,"VI":12,"V":43},"b":{"I":90,"II":98,"III":54,"VI":72,"V":13},"c":{"I":30,"II":20,"III":50,"VI":22,"V":40}}
dict2={"a":{"I":34,"II":71,"III":94,"VI":32,"V":63},"b":{"I":50,"II":48,"III":24,"VI":92,"V":43},"c":{"I":31,"II":22,"III":54,"VI":82,"V":49}}
def1=pd.DataFrame(dict1)
def2=pd.DataFrame(dict2)
def3=def1.rsub(def2)#rsub() meaning subtraction but reverse simillary
print(def3)         #radd(),rmul,rdiv

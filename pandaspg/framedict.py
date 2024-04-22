#nested dictionary
import pandas as pd
dict={"employee1":{'name':'raj','age':45,'salary':15000},'employee2':{'name':'teena','age':34,'salary':150000}}
print(dict)
frm1=pd.DataFrame(dict)
print(frm1)
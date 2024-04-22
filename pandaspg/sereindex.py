import pandas as pd
import numpy as np
arr=['b','e','f','d','a','b']
myval=[300,200,400,700,100,600]
obj1=pd.Series(index=arr,data=myval)
print(obj1)
obj1['c']=788
print(obj1)
obj1[0:2]=[111,345]
print(obj1)
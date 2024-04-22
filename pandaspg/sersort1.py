import pandas as pd
import numpy as np
arr=['b','e','f','d','a','b']
myval=[300,200,400,700,100,600]
obj1=pd.series(index=arr,data=myval)
print(obj1)
print('asscending series by index:-')
print(obj1.sort_index())
print('descending series by index')
print(obj1.sort_index(asscending=False))
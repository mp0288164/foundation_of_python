import pandas as pd
import numpy as np
arr=['b','e','f','d','a','b']
myval=[300,200,400,700,100,600]
obj1=pd.series(index=arr,data=myval)
print(obj1)
print('asscending series by value:-')
print(obj1.sort_values())
print('descending series by value')
print(obj1.sort_values(asscending=False))
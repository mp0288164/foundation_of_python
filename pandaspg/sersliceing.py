#import pandas and numpy
import pandas as pd
import numpy as np
#atributesof series
arr=[1,2,3,4,5]
myval=[1000,2000,3000,4000,np.NaN]
obj1=pd.series(index=arr,data=myval)
print(obj1)
#serise slicing
print(obj1[1:])
print(obj1[0:3])
print(obj1[0:4:2])
print(obj1[0::4])
print(obj1[0::2])
print(obj1[1:3])

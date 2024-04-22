#import pandas and numpy
import pandas as pd
import numpy as np
#atributesof series
arr=[1,2,3,4,5]
myval=[1000,2000,3000,4000,np.NaN]
obj1=pd.Series(index=arr,data=myval)
print(obj1)
print(obj1.values)
print(obj1.hasnans)
print(obj1.nbytes)
print(obj1.size)
print(obj1.shape)
print(obj1.ndim)
print(obj1.dtype)
print(obj1.items)

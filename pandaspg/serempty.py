#import pandas and numpy
import pandas as pd
import numpy as np
#atributesof series
arr=[1,2,3,4,5]
myval=[1000,2000,3000,4000,np.NaN]
obj1=pd.Series(index=arr,data=myval)
print(obj1)
print(obj1.empty)#return true if obj1 is empty anthor false
obj2=pd.Series()
print(obj2.empty)
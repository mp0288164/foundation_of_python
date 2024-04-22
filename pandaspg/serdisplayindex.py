#import pandas and numpy
import pandas as pd
import numpy as np
#atributesof series
arr=[1,2,3,4,5]
myval=[1000,2000,3000,4000,np.NaN]
obj1=pd.Series(index=arr,data=myval)
print(obj1)
#particular index value display
print(obj1[3],obj1[5])

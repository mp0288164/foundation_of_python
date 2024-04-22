#import pandas and numpy
import pandas as pd
import numpy as np
arr=[1,2,3,4,5]
myval=[1000,2000,3000,4000,np.NaN]
obj1=pd.series(index=arr,data=myval,dtype=np.float32)
print(obj1)
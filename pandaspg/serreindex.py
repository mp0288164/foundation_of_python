import pandas as pd
import numpy as np
arr=['b','e','f','d','a','b']
myval=[300,200,400,700,100,600]
obj1=pd.series(index=arr,data=myval)
print(obj1)
obj2=obj1.reindex(['a','c','b','f','e','d'])
print(obj2)
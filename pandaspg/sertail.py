#import pandas and numpy
import pandas as pd
import numpy as np
arr=['a','b','c','d','e','f']
myval=[100,200,300,400,500,600]
obj1=pd.series(index=arr,data=myval)
print(obj1)
#tail() method of series for displaying rows
print("tail with default raw:-")
print(obj1.tail())#default last 5 rows are showing
print("tail method of specified rows")
print("obj1.tail(3)")

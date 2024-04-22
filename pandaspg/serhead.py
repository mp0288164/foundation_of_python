#import pandas and numpy
import pandas as pd
import numpy as np
#atributesof series
arr=['a','b','c','d','e','f']
myval=[100,200,300,400,500,600]
obj1=pd.series(index=arr,data=myval)
print(obj1)
#head()method of series in using displaying row
print("headwith defalut row:-")
print(obj1.head())#default starting 5 rows are display
print("head with specified row")
print(obj1.head(2))

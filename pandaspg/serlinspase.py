#import numpy and pandas
import padas as pd
import numpy as np
"""linspase() method of numpy.linspase() method are take three argument(startpoint,endpoit,no ofparts)"""

lin=np.linspase(1,10,3)
obj1=pd.series(lin)
print(obj1)
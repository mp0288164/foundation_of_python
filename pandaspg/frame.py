#create data frame with the help of list
import pandas as pd
#nested list
list=[[1,2,3],[4,5,6],[7,8,9]]
frm=pd.DataFrame(list)
print(frm)
frm1=pd.DataFrame(list,index=[1,2,3])
print(frm1)
frm1=pd.DataFrame(list,index=[1,2,3],columns=['A','B','C'])
print(frm1)
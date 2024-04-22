#frame() funtion in pandas
#why using frame?
"""represent data form of 2d(two dimentional<row&cloumn>)."""
#import pandas libreary
import pandas as pd
#create dictionary
dict={"student":["anil","shubham","teena","reena","seema"],"sportsmarks":[56,78,90,76,89],"marks":[450,456,485,490,498]}
print(dict)
n=pd.DataFrame(dict)
print(n)
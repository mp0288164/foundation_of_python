#read() method
myfile=open("e://pythonpg//studinfo.txt","r")
str=myfile.read()#read(5)<-- means read only starting 5byte
print(str)
myfile.close()
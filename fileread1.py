#read method
file=open("e://pythonpg//studinfo.txt","r")
str=file.read(5)#read 5 byte only
print(str)
n=file.read()
print(n)
file.close()

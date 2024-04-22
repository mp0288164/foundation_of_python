#filehandlling
#readline() method
file=open("e://pythonpg//studinfo.txt","r")
str1=""
size=0
tsize=0
while str1:
	str1=file.readline()
	tsize=tsize+len(str1)
	size=size+len(str1.strip())
print("size of file after removing all EOL char&blanklines:-",size)
print("the total size of file:-",tsize)
file.close()
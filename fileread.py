#filehandlling
#read data from file
file=open("e://pythonpg//studinfo.txt","r")
for line in file:
	print(line,end="")
file.close()
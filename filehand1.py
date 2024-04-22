#file handlling
#write open in writemode
#open() function for fileopen, write() function for write in file
myfile=open("e://pythonpg//studinfo.txt","w")
for i in range(5):
	name=input("enter the name:-")
	myfile.write(name)
	myfile.write('\n')
myfile.close()
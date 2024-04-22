#filehandlling
#data write in file
myfile=open("e://pythonpg//studinfo.txt","w")
for i in range(5):
	name=input("enter the student name:-")
	myfile.write(name)
	myfile.write("\n")
myfile.close()
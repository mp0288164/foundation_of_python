#filehandlling
#openfile in read-mode
myfile=open("e://pythonpg//studinfo.txt","r")
for line in myfile: #line is keyword or read file line by line
	print(line,end=" ")
myfile.close()
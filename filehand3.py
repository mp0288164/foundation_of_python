#write data in file from of (like-->list,dictionary)
myfile=open("e://pythonpg//studinfo.txt","w")
list=[]
for i in range(5):
	name=input("enter the name:-")
	list.append(name+"\n")
print(list)
myfile.writelines(list)#writelines() function are using
myfile.close
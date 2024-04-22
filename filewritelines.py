#write data in file from of list,dictionary
file=open("e://pythonpg//studinfo.txt","w")
l=[]
for i in range(5):
	n=input("enter the name:-")
	l.append(n+"\n")
print(l)
file.writelines(l)
file.close()








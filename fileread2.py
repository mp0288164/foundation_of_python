file1=open("e://pythonpg//marks.dat","r")
for line in file1:
	list=line.split(",")
	print("rollno:-",list[0])
	print("name:-",list[1])
	print("marks:-",list[2])
f.close()
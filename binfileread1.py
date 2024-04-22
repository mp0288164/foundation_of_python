import pickle
f=open("student1.txt","rb")
print("read data form a file")
try:
	while True:
		data=pickle.load(f)
		for r in data:
			print("rollno:-",r[0])
			print("name:-",r[1])
			print("marks:-",r[2])
			print("persantage:-",r[3])
except EOFError ae e:
	fr.close()

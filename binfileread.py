import pickle
f=open("student1.txt","rb")
print("read data froma file")
try:
	while True:
		data=pickle.load(f)
		for r in data:
			print("rollno:-",r[0])
			print("name:-",r[1])
			
			print("total:-",r[2])
			print("persantage:-",r[3])
except EOFError as e:
	f.close()
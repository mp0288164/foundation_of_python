import pickle
f=open("student1.txt","rb")
rollno=int(input("enter the rollno if want to read:-"))
found=0
try:
	while True:
		data=pickle.load(f)
		for r in data:
			if r[0]==rollno:
				print("rollno:-",r[0])
				print("name:-",r[1])
				print("marks:-",r[2])
				print("persantage:-",r[3])
				found=1
				
except Exception:
	f.close()
if found==0:
	print("record not found")
	
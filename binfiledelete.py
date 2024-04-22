import pickle
import os
f=open("student1.txt","rb")
f1=open("temp32.txt","wb")
print("delete record from a file")
rollno=int(input("enter the rollno if you want to delete:- "))
found=0
try:
	while True:
		data=pickle.load(f)
		for r in data:
			if r[0]==rollno:
				found=0
				continue
		pickle.dump(data,f1)
except Exception:
	f.close()
	f1.close()
os.remove("student1.txt")
os.rename("temp32.txt","student1.txt")
if found==1:
	print("record deleted successfully")
else:
	print("record not foundin file")
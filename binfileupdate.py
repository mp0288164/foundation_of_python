import os
import pickle
f=open("student1.txt","rb")
f1=open("temp32.txt","wb")
print("update/modify record in file")
rollno=int(input("enter the rollno,if you want to update record:-"))
found=0
try:
	while True:
		data=pickle.load(f)
		if data[0][0]==rollno:
			data[0][1]=input("enter the new name:-")
			data[0][2]=int(input("enter the new marks:-"))
			found=1
		pickle.dump(data,f1)
except Exception:
	f.close()
	f1.close()
os.remove("student1.txt")
os.rename("temp32.txt","student1.txt")
if found==1:
	print("record updated succesfully")
else:
	print("reocrd not found in file")


#binaryfile--> data read and write
import pickle
f=open("student1.txt","wb")
print("write data")
ch="y"
while ch=="y":
	data=[]
	rollno=int(input("enter the rollno:-"))
	sname=input("enter the name:-")
	marks=float(input("enter the marks:-"))
	per=marks/5
	data.append([rollno,sname,marks,per])
	pickle.dump(data,f)
	ch=input("do you want to enter more record y/n:-")
f.close()
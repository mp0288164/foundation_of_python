import pickle
f=open("student1.txt","ab")
print("append data")
ch="y"
while ch=="y":
	data=[]
	rollno=int(input("enter student rollno:-"))
	name=input("enter student name:-")
	marks=float(input("enter the marks:-"))
	per=marks/5
	print("persantage:-",per)
	data.append([rollno,name,marks,per])
	pickle.dump(data,f)
	ch=input("do you want to enter more record y/n:-")
f.close
import pickle
import os
class student:
	def getdata(self):
		self.rollno=int(input("enter the rollno:-"))
		self.name=input("enter the name")
		self.marks=int(input("enter the marks:-"))
		self.per=self.marks/5
#__main__
import pickle
k=student()
f=open("student1.txt","wb")
ch="y"
while ch=='y':
	k.getdata()
	pickle.dump(k,f)
	ch=input("do you want to enter more data y/n:-")
f.close()

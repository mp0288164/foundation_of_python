import pickle
import os
class student:
	def __init__(self):
		self.rollno=0
		self.name=""
		self.marks=0
		self.per=self.marks/5
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("marks:-",self.marks)
		print("persantage:-",self.per)
#__main__
k=student()
f=open("studinfo.txt","rb")
f1=open("temp.txt","wb")
srollno=int(input("enter the rollno which you want to delete:-"))
found=0
try:
	while True:
		k=pickle.load(f)
		if srollno==k.rollno:
			found=1
			continue
		pickle.dump(k,f1)
except Exception:
	f.close()
	f1.close()
os.remove("studinfo.txt")
os.rename("temp.txt","studinfo.txt")
if found==1:
	print("record deleted successfully")
else:
	print("recordnot found")
			
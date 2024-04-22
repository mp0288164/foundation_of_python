import pickle
class student:
	def __init__(self):
		self.rollno=0
		self.name=""
		self.marks=0
		self.per=0
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("marks:-",self.marks)
		print("persantage:-",self.per)
#__main__
k=student()
f=open("student1.txt","rb")
found=0
srollno=int(input("enter the rollno:-"))
try:
	while True:
		k=pickle.load(f)
		if srollno==rollno:
			k.display()
			found=1
			break
except Exception:
	f.close()
if found==1:
	print("record is found in file")
else:
	print("record not found in file")

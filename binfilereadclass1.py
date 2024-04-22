import pickle
class student:
	def __init__(self):
		self.rollno=0
		self.name=" "
		self.marks=0
		self.per=0
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("marks:-",self.marks)
		print("persantage:-",self.per)
	def putrollno(self):
		return self.rollno
#__main__
k=student()
f=open("student1.txt","rb")
srollno=int(input("enter the rollno which want you delete:-"))
found=0
try:
	while True:
		k=pickle.load(f)
		if srollno==k.putrollno():
			k.display()
			found=1
			break
except Exception:
	f.close()
if found==1:
	print("record deleted successfully")
else:
	print("record not found")
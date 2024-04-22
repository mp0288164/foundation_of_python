#binary data read and write using class
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
#__main__
k=student()
f=open("student1.txt","rb")
try:
	while True:
		k.pickle.load(f)
		k.display()
except Exception:
	f.close()
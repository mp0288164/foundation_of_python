# inheritance with method overriding
class student:
	def getdata(self,r,str):
		self.rollno=r
		self.name=str
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
class marks(student):
	def getmarks(self,p,c,m):
		self.phy=p
		self.che=c
		self.maths=m
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("physics:-",self.phy)
		print("chemistry:-",self.che)
		print("mathemetics:-",self.maths)
#__main__
s=student()
s.getdata(1234,"shubham")
s.display()
k=marks()
k.getdata(234,"manisha")
k.getmarks(43,56,87)
k.display()

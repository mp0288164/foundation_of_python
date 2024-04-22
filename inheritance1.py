#single level Inheritance
#using  public mode
class student:
	def getdata(self,x,y):
		self.rollno=x
		self.name=y
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
#__main__
k=marks()
k.getdata(124,"weeni")
k.getmarks(89,90,67)
k.display()
print("rollno:-",k.rollno)
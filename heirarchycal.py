class student:
	def getdata(self,r,str):
		self.rollno=r
		self.name=str
class science(student):
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
class commarce(student):
	def getmarks(self,e,a,b):
		self.eco=e
		self.acc=a
		self.bus=b
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("economics:-",self.eco)
		print("account:-",self.acc)
		print("business:-",self.bus)
#__main__
s=science()
c=commarce()
s.getdata(12354,"sunil")
s.getmarks(45,67,89)
c.getdata(1234,"nidhi")
c.getmarks(23,56,78)
s.display()
c.display()
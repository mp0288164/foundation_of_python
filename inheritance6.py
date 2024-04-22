#multilevel inheritance
class student:
	def getdata(self,r,s):
		self.rollno=r
		self.name=s
class marks(student):
	def getmarks(self,p,c,m):
		self.phy=p
		self.che=c
		self.maths=m
class calculation(marks):
	def calculate(self):
		self.total=self.phy+self.che+self.maths
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("physics:-",self.phy)
		print("chemistry:-",self.che)
		print("mathemetics:-",self.maths)
		print("total:-",self.total)
#__main__
k=calculation()
k.getdata(1234,"mahi")
k.getmarks(23,65,98)
k.calculate()
k.display()
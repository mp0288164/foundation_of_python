class student:
	def getdata(self,r,str):
		self.rollno=r
		self.name=str
class sports(student):
	def getsportsmarks(self,s):
		self.sportsmarks=s
class marks(student):
	def getmarks(self,p,c,m):
		self.phy=p
		self.che=c
		self.maths=m
class calculation(marks,sports):
	def calculate(self):
		self.total=self.phy+self.che+self.maths+self.sportsmarks
		self.per=self.total/4                       
	def display(self):
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("physics:-",self.phy)
		print("chemistry:-",self.che)
		print("mathemetics:-",self.maths)
		print("totalmarks:-",self.total)
		print("persantage:-",self.per)
#___main__
k=calculation()
k.getdata(1234,"manisha")
k.getmarks(90,98,87)
k.getsportsmarks(90)
k.calculate()
k.display()
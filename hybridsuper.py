class student:
	def __init__(self,r,str):
		self.rollno=r
		self.name=str
class sportsmarks(student):
	def __init__(self,r,str,s):
		super().__init__(r,str)
		self.sportsmarks=s
class marks(student):
	def __init__(self,r,str,p,c,m):
		super().__init__(r,str)
		self.phy=p
		self.che=c
		self.maths=m
class calculation(sportsmarks,marks):
	def __init__(self,r,str,s,p,c,m):
		super().__init__(r,str,s,p,c,m)
		self.total=self.sportsmarks+self.phy+self.che+self.maths
		self.per=self.total/4
	def display():
		print("rollno:-",self.rollno)
		print("name:-",self.name)
		print("sportsmarks:-",self.sportsmarks)
		print("physics:-",self.phy)
		print("chemistry:-",self.phy)
		print("mathemetics:-",self.maths)
		print("totalmarks:-",self.total)
		print("persatage:-",self.per)
#__main__
k=calculation(1234,"manisha",90,98,99,97)
k.display()		
		
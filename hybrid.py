class student:
	def getdata(self,r,str):
		self.__rollno=r
		self.__name=str
	def putrollno(self):
		return self.__rollno
	def putname(self):
		return self.__name
class sports(student):
	def getsportsmarks(self,s):
		self.__sm=s
	def putspm(self):
		return self.__sm
class marks(student):
	def getmarks(self,p,c,m):
		self.phy=p
		self.che=c
		self.maths=m
class calculation(sports,marks):
	def calculate(self):
		self.t=self.phy+self.che+self.maths
	def display(self):
		print("rollno is:-",self.putrollno())
		print("name:-",self.putname())
		print("sportsmarks:-",self.putspm)
		print("physics:-",self.phy)
		print("chemistry:-",self.che)
		print("mathemetics:-",self.maths)
		print("total of all marks:-",self.t)
#__main__
k=calculation()
k.getdata(1234,"gara")
k.getsportsmarks(90)
k.getmarks(56,78,98)
k.calculate()
k.display()		
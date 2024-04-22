#multilevel inheritance
#with private and protected mode
class student:
	def getdata(self,r,s):
		self.__rollno=r
		self._name=s
	def putrollno(self):
		return self.__rollno
class marks(student):
	def getmarks(self,p,c,m):
		self.__phy=p
		self.__che=c
		self._maths=m
	def putphy(self):
		return self.__phy
	def putche(self):
		return self.__che
class calculation(marks):
	def calculate(self):
		self.__total=self.putphy()+self.putche()+self._maths
	def display(self):
		print("rollno:-",self.putrollno())
		print("name:-",self._name)
		print("physics:-",self.putphy())
		print("chemistry:-",self.putche())
		print("mathemetics:-",self._maths)
		print("total:-",self.__total)
#__main__
k=calculation()
k.getdata(1234,"mahi")
k.getmarks(23,65,98)
k.calculate()
k.display()
#singlelevel inheritance 
#private protected mode
class student:
	def getdata(self,x,y):
		self.__rollno=x
		self._name=y
	def putrollno(self):
		return(self.__rollno)
class marks:
	def grtmarks(self,p,c,m):
		self.__phy=p
		self.__che=c
		self.__math=m
	def display(self):
		print("RollNo.:-",self.putrollno())
		print("Name is:-",self._name)
		print("physics:-",self__phy)
		print("chemistry:-",self__che)
		print("mathemetics:-",self__math)
#__main__
k=marks()
k.getdata(124,"sunil")
k._name("ritu")
k.getmarks(56,78,90)
k.display
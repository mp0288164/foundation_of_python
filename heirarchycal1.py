#heirarachycal inheritance private protrcted mode
class student:
	def getdata(self,r,str):
		self.__rollno=r
		self.__name=str
	def putrollno(self):
		return self.__rollno
	def putname(self):
		return self.__name
class science(student):
	def getmarks(self,p,c,m):
		self.__phy=p
		self.__che=c
		self._maths=m
	def putphy(self):
		return self.__phy
	def putche(self):
		return self.__che
	def display(self):
		print("rollno:-",self.putrollno())
		print("name:-",self.putname())
		print("physics:-",self.putphy())
		print("chemistry:-",self.putche())
		print("mathemetics:-",self._maths)
class commarce(student):
	def getmarks(self,e,a,b):
		self.__eco=e
		self.__acc=a
		self.__bus=b
	def display(self):
		print("rollno:-",self.putrollno())
		print("name:-",self.putname())
		print("economics:-",self.__eco)
		print("account:-",self.__acc)
		print("business:-",self.__bus)
#__main__
s=science()
c=commarce()
s.getdata(12354,"sunil")
s.getmarks(45,67,89)
c.getdata(1234,"nidhi")
c.getmarks(23,56,78)
s.display()
c.display()
#heirarachycal inheritance private protrcted mode
#using constructor __init__() method
class student:
	def __init__(self,r,str):
		self.__rollno=r
		self.__name=str
	def putrollno(self):
		return self.__rollno
	def putname(self):
		return self.__name
class science(student):
	def __init__(self,r,str,p,c,m):
		student.__init__(self,r,str)
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
	def __init__(self,r,str,e,a,b):
		super(). __init__(r,str)
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
s=science(1234,"manisha",12,34,56)
c=commarce(1235,"shubham",234,678,890)
s.display()
c.display()
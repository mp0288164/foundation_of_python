class student:
	def __init__(self,x,y):
		self.__rollno=x
		self._name=y
	def putrollno(self):
		return(self.__rollno)
class marks(student):
	def __init__(self,r,s,p,c,m):
		student.__init__(self,r,s)
		self.__phy=p
		self.__che=c
		self.__maths=m
	def display(self):
		print("rollno:-",self.putrollno())
		print("name:-",self._name)
		print("physics:-",self.__phy)
		print("chemistry:-",self.__che)
		print("mathemetics:-",self.__maths)
#___main___
k=marks(124,"shubham",32,65,87)
k.display()
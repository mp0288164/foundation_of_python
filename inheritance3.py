#singlelevel inheritance with using constrictor method __init__()
class student:
	def __init__(self,x,y):
		self.__rollno=x
		self._name=y
	def putrollno(self):
		return(self.__rollno)
class marks(student):
	def __init__(self,r,s,p,c,m):
		super().__init__(r,s)
		self.__phy=p
		self.__che=c
		self.__math=m
	def display(self):
		print("rollno:-",self.putrollno())
		print("name:-",self._name)
		print("physics:-",self.__phy)
		print("chemistry:-",self.__che)
		print("mathemetics:-",self.__math)
#__main__
k=marks(124,"sunil",56,78,99)
k.display()
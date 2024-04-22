#multilevel inheritance
#with private and protected mode
#using constructor method __init__()
class student:
	def __init__(self,r,s):
		self.__rollno=r
		self.__name=s
	def _putrollno(self):
		return self.__rollno
	def putname(self):
		return self.__name
class marks(student):
	def __init__(self,r,s,p,c,m):
		super(). __init__(r,s)
		self.__phy=p
		self.__che=c
		self._maths=m
	def putphy(self):
		return self.__phy
	def putche(self):
		return self.__che
class calculation(marks):
	def __init__(self,r,s,p,c,m):
		super(). __init__(r,s,p,c,m)
		self.__total=self.putphy()+self.putche()+self._maths
	def display(self):
		print("rollno:-",self._putrollno())
		print("name:-",self.putname())
		print("physics:-",self.putphy())
		print("chemistry:-",self.putche())
		print("mathemetics:-",self._maths)
		print("total:-",self.__total)
#__main__
k=calculation(1234,"mahi",32,56,87)
k.display()
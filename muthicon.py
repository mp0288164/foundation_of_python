#method order/constructor order resolution
#multiple inheritance with constructor
# multiple inheritance ke concept me program me subclass se superclass ke constructor ko call kiya jata h but multiple inheritance ke concept me do super class hoti h or #dono super class apni super class object class(jo ki kisi bhi super class ki by default superclass hoti h)ke constructor ko call karti h pr object class me constructor ka koi #object nhi hota h to jab subclass se super class ka constructor call kiya jata h to subclass me inherit superclass(student,sports)to leftside wali class ka constuctor call hota h.
class student:
	def __init__(self,r,str,s):
		super().__init__(s)
		self.__rollno=r
		self.name=str
	def putrollno(self):
		return self.__rollno
class sports:
	def __init__(self,s):
		super().__init__()
	def putsportmarks(self):
		return self.__sportsmarks
class marks(student,sports):
	def __init__(self,r,str,s,p,c,m):
		super().__init__(r,str,s)
		self.__phy=p
		self.__che=c
		self.__maths=m
	def display(self):
		print("rollno is:-",self.putrollno())
		print("name is:-",self.name)
		print("marks of physics:-",self.__phy)
		print("marks of chemistry:-",self.__che)
		print("marks of mathemetics:-",self.__maths)
#__main__
k=marks(1234,"manisha",56,78,90,90)
k.display()

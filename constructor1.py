#constructor
class add:
	def __init__(self,x,y):
		self.a=x
		self.b=y
	def calculate(self):
		return(self.a+self.b)
#__main__
k=add(5,6)
m=add(2.3,5.4)
print("sum:-",k.calculate())
print("sum:-",m.calculate())
	
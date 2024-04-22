#constructor overloading
#this program will give error because two init method in class not possible,override first init methos by second init method
class record:
	def __init__(self,x):
		self.a=x
		self.b=y
	def __init__(self,x,y):
		self.a=x
		self.b=y
	def display(self):
		print("a:-",self.a)
		print("b:-".self.b)
#__main__
k=record()
m=record()
k.display()
m.display()

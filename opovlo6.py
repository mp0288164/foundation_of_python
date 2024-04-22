class add:
	a=None
	def getno(self,x):
		self.a=x
	def __add__(self,p):
		print("addition is:-",self.a+p.a)
#__main__
k=add()
m=add()
k.getno(12)
m.getno(12)
k+m
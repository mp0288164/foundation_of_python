class multi:
	a=None
	def getno(self,x):
		self.a=x
	def __mul__(self,p):
		return self.a*p.a
#__main__
k=multi()
m=multi()
k.getno(65)
m.getno(1000)
q=k*m
print("multiplication is:-",q)
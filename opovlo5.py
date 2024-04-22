class nequal:
	a=None
	def getno(self,x):
		self.a=x
	def __ne__(self,p):
		if self.a!=p.a:
			print("first object is not equal to second object")
		else:
			print("first object is equal to second object")
#__main__
k=nequal()
m=nequal()
k.getno(12)
m.getno(12)
k!=m
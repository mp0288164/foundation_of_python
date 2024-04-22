class truediv:
	a=None
	def getno(self,x):
		self.a=x
	def __truediv__(self,p):
		q=truediv()
		q.self=self.a/p.a
		return q.self
#__main__
k=truediv()
m=truediv()
k.getno(90)
m.getno(10)
r=k/m
print("division is:-",r)
		
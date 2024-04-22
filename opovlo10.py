class floordiv:
	a=None
	def getno(self,x):
		self.a=x
	def __floordiv__(self,p):
		q=floordiv()
		q.self=self.a//p.a
		return q.self
#__main__
k=floordiv()
m=floordiv()
k.getno(90)
m.getno(10)
r=k//m
print("division is:-",r)
		
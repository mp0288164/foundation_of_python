class less:
	a=None
	def getno(self,x):
		self.a=x
	def __lt__(self,p):
		if self.a<p.a:
			print("first object is less than second object")
		else:
			print("second object is less than is second object")
#__main__
s=less()
m=less()
s.getno(23)
m.getno(90)
s<m # s.gt(m). lessthan operator overload
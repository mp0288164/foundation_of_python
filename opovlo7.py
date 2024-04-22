class sub:
	a=None
	def getno(self,x):
		self.a=x
	def __sub__(self,p):
		print("subtraction is:-",self.a+p.a)
#__main__
k=sub()
m=sub()
k.getno(689)
m.getno(789)
k-m
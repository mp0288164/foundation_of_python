class mod:
	a=None
	def getno(self,x):
		self.a=x
	def __mod__(self,p):
		print("modulo division:",self.a%p.a)
		
		
	
#__main__
k=mod()
m=mod()
k.getno(900)
m.getno(67)
k%m

		
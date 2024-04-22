class great:
	a=None
	def getno(self,x):
		self.a=x
	#operator overload
	def __gt__(self,p):
		if self.a>p.a:
			print("first object is greater than second object")
		else:
			print("second object is greater than first object")
#__main__
s=great()
m=great()
s.getno(12)
m.getno(18)
s>m #s.gt(m)

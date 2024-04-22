class equal:
	a=None
	def getno(self,x):
		self.a=x
	# equal-to operator overload
	def __eq__(self,p):
		if self.a==p.a:
			print("first object is equal to second object")
		else:
			print("first object is not equal to second object")
#__main__
s=equal()
m=equal()
s.getno(18)
m.getno(18)
s=m #s.eq(m)calling def __eq__()fuction

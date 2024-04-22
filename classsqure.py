class squre:
	def sqr(self,x):
		self.a=x
		return self.a*self.a
#_main_
n=int(input("enter the no:-"))
k=squre()
s=k.sqr(n)
print("squre is:-",s)
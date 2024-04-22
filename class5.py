class greater:
	def gre(self,x,y):
		self.a=x
		self.b=y
		if self.a<self.b:
			print("greatest no is:-",self.b)
		else:
			print("greatest no is:-",self.a)
#__main__
m=int(input("enter the numbers:-"))
n=int(input("enter the numbers:-"))
g=greater()
g.gre(m,n)
class addcomplex:
	real=None
	image=None
	def getdata(self,x,y):
		self.real=x
		self.image=y
	def putdata(self):
		print("real:-",self.real)
		print("image:-",self.image)
	def __isub(self,p):
		self.real=self.real+p.real
		self.image=self.image+p.self
		return self
#__main__
k=addcomplex()
m=addcomplex()
k.getdata(2.3,4.3)
m.getdata(9.0,8.9)
k.putdata()
m.putdata()
k-=m
print("addition is:-")
k.putdata()
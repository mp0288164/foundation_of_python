#returning object
class complex:
	real=None
	image=None
	def getdata(self,x,y):
		self.real=x
		self.image=y
	def putdata(self):
		print("real is:-",self.real)
		print("image  is:-",self.image)
	def calculate(self,p):
		k=complex()
		k.real=self.real+p.real
		k.image=self.image+p.image
		return k
#__main__
s=complex()
m=complex()
q=complex()
s.getdata(4.5,3.4)
m.getdata(2.3,4.3)
q=s.calculate(m)
s.putdata()
m.putdata()
q.putdata()

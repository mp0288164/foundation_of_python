#object as aargument
class copy:
	a=None
	b=None
	def getdata(self,x,y):
		self.a=x
		self.b=y
	def putdata(self):
		print("a=",self.a)
		print("b:-",self.b)
	def copobj(self,p):
		self.a=p.a
		self.b=p.b
#__main__
k=copy()
s=copy()
k.getdata(5,8)
s.copobj(k)
k.putdata()
s.putdata()
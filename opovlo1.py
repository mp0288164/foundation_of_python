#operator overloading
class complex:
	real=None
	image=None
	def getdata(self,x,y):
		self.real=x
		self.image=y
	def putdata(self):
		print("real:-",self.real)
		print("image:-",self.image)
	#predefine function for operator overloading
	def __add__(self,p):
		q.complex()
		q.real=self.real+p.real                  
		q.image=self.image+p.image
		return q.real,q.image
#__main__
k=complex()
m=complex()
s=complex()
k.getdata(12,36)
m.getdata(12,36)
s=k+m #call def__add__() predefine function
k.putdata()
s.putdata()
m.putdata()
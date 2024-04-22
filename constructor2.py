class calculation:
	def __init__(self,oper,*l):
		self.optype=oper
		self.k=l
	def calculate(self):
		if self.optype=="circle":
			return(3.14*self.k[0]*self.k[0])
		elif self.optype=="ractangle":
			return(self.k[0]*self.k[1])
		elif self.optype=="triangle":
			return(1/2*self.k[0]*self.k[1])
#__main__
k=calculation('circle',2.5)
m=calculation("ractangle",2.3,4.5)
s=calculation("triangle",2.3,5.6)
print("area of circle is:-",k.calculate())
print("area of triangle is:-",s.calculate())
print("area of ractangle is:-",m.calculate())

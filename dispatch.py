#method overloading
#dispatch method
from multipledispatch import dispatch
class calculation:
	@dispatch(float)
	def calculate(r):
		area=3.14*r*r
		return area
	@dispatch(float,float)
	def calculate(l,b):
		return (l*b)
	@dispatch(float,float,float)
	def calculate(hlaf,h,b):
		return (half*h*b)
#__main__
p=calculation()
k=calculate()
s=calculate()
print("area of circle:-",p.calculate(2.3))
print("area of ractangle:-",k.cakculate(2.3,4.5))
print("area od triangle:-",s.calculate(2.5,1.2,6.7))
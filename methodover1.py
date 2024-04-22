#polymorphism
#method overloading
class multiply:
	def calculate(self,x,y):
		self.ans=x*y
		print("multiplication is:-",self.ans)
class addition:
	def calculate(self,x,y):
		self.ans=x+y
		print("addition is:-",self.ans)
#__main__
m=multiply()
a=addition()
for i in (m,a):
	i.calculate(int(input("enter the first no:-")),int(input("enter the first no:-")))
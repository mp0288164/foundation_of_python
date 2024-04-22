#polymorphism
#same thing but different behave.
#two types of polymorphism
#1.complie time polymorphism
#staic binding or early binding
#a.method overloading
#b.operator overloading
#2.run time polymorphism
#run time polymorphism achive  by "inheritance"
#__method overloading__

class multiply:
	def calculate(self,x,y):
		self.ans=x*y
		print("multiplication:-",self.ans)
class addition:
	def calculate(self,m,n):
		self.ans=m+n
		print("addition:-",self.ans)
#_main_
p=multiply()
k=addition()
for i in (p,k):
	i.calculate(int(input("enter the first no;-")),int(input("enter the first no:-")))
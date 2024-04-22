class add:
	def getdata(self,x,y):
		self.a=x
		self.b=y
	def calculate(self):
		return self.a+self.b
#_main_
a=add()
n=int(input("enter the no:-"))
m=int(input("enter the no:-"))
a.getdata(m,n)
print("answer is:-",a.calculate())
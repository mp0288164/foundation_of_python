class add:
	def getdata(self,x,y):
		self.a=x
		self.b=y
		return self.a+self.b
#__main__
ad=add()
n=int(input("enter the first no:-"))
m=int(input("enter the second no:-"))
k=print("sum of :-",ad.getdata(m,n))
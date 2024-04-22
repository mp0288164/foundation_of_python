class swap:
	def getdata(self,x,y):
		self.a=x
		self.b=y
	def exchange(self):
		self.a,self.b=self.b,self.a
	def putdata(self):
		print("a:-",self.a)
		print("b:-",self.b)
#__main__
k=swap()
k.getdata(12,34)
k.putdata()
k.exchange()
k.putdata()
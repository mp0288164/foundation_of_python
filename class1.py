#class is a collection of userdife datatype,variables and mehods,encapsulation
class add:
	def getdata(self,x,y):
		self.a=x
		self.b=y
	def putdata(self):
		print("a:-",self.a)
		print("b:-",self.b)
#_main_
k=add()
k.getdata(12,34)
k.putdata()
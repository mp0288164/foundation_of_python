#constructor and destructor
#__init__() or __del__()
#using static variable concept
class conAnddes:
	num=0
	def __init__(self,v):
		conAnddes.num+=1
		self.var=v
		print("The Object Value is:-",self.var)
	def __del__(self):
		conAnddes.num-=1
		print("No of Object with Value %d is delete"%self.var)
#__main__
k=conAnddes(6)
s=conAnddes(5)
m=conAnddes(8)

class calculation:
	def calculate(self,areatype,*r):
		if areatype=="circle":
			self.area=3.14*r[0]
			return self.area
		elif areatype=="ractangle":
			self.area=r[1]*r[2]
			return self.area
		else:
			self.area=1\5*[1]*[2]
			return self.area
#__main__
k=calculation()
m=calculation()
t=calculation()
print("Area of circle:-",k.calculate("circle",2.5))                                  
print("Area of ractangle:-",m.calculate("ractangle",8.9,90.0))
print("Area of triangle is:-",t.calculate("triangle is:-","triangle",3.5,4.6))
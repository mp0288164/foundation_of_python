def qube(self,x):
	for i in x:
		y=i*i*i
		x=x-1
		return y
#__main__
k=qube
n=int(input("entrer the number:-"))
print("Qube is:-",k)
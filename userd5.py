#Function with named argument
def interest(p,r,t):
	return p*r*t/100
#_main_
print("interest is:-",interest(p=1000,r=3.0,t=12))
print("interest is:-",interest(r=3.0,p=1000,t=12))
print("interest is:-",interest(t=12,r=3.0,p=1000))

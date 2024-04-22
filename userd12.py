#m^n
def power(x,y):
	if y==1:
		return x
	else:
		return (x*power(x,y-1))
#_main_
m=int(input("enter the value of m:-"))
n=int(input("enter the value of n:-"))
print("answer is:-",power(m,n))

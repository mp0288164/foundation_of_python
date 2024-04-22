#sum of natural no(1,2,3,4,...........)
def nsum(x):
	if x==1:
		return 1
	else:
		return (x+nsum(x-1))
#_main_
n=int(input("enter the range:-"))
print("sum of natural no:-",nsum(n))
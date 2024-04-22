def fact(x):
	k=1
	while x>0:
		k=k*x
		x-=1
	return k
#_main_
n=int(input("enter any no :-"))
print("factorial is:-",fact(n))
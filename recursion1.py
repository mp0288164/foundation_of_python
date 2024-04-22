#RECURSION
#find factorial with help of recursion
def fact(x):
	if x==1:
		return 1
	else:
		return(x*fact(x-1))
#_main_
n=int(input("enter the no:-"))
print("factorial is:-",fact(n))
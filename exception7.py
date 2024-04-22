try:
	from fact1 import fact
	n=int(input("enter the number,you find factorial:-"))
	print("factorial of:-",fact(n))
except ModuleNotFoundError as e:
	print("error is:-",e)
print("I am here")
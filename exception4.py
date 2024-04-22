a=int(input("enter the first number:-"))
try:
	c=a+b
	print("sum:-",c)
except NameError as e:
	print("error:-",e)
print("IN AM HERE")
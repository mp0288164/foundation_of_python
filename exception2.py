try:
	n=int(input("enter the first number:-"))
	m=int(input("enter the second number:-"))
	c=m+n
	print("sum:-",c)
except ValueError as a:
	print("error",a)
print("I AM HERE")
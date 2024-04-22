#raise
try:
	a=int(input("enter the first no:-"))
	b=int(input("enter the second no:-"))
	if b==0:
		raise ZeroDivisionError
	c=a/b
	print("divide is:-",c)
except ZeroDivisionError as e:
	print("error is:-",e)

print("i am here")
try:
	a=int(input("enter the first number:-"))
	b=int(input("enter the second number:-"))
	c=a/b
	print("division is:-",c)
except ZeroDivisionError as e:
	print("error is:-",e)
else:
	print("i am else block. i am execute no error found in try block")
finally:
	print("i am finally block. iam execute any situation:-no error found in try block,error found in try block,error are no except by try block etc yet finally block are execute any situation")
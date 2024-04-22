a=int(input("enter the first no:-"))
b=int(input("enter the second no:-"))
c=int(input("enter the third no:-"))
if a>b:
	if a>c:
		print("a is greatest no. :-",a)
	else:
		print("c is greatest no. :-",c)
else:
	if b>a:
		if b>c:
			print("b is greatest no. :-",b)
		else:
			print("c is greatest no. :-",c)

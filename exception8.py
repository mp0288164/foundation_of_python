try:
	n=int(input("enter the first number:-"))
	m=int(input("enter the second number:-"))
	k=n/m
	print("answer is:-",k)
	l=[1,3,4,5,5,6,]
	print("list is:-",l)
	print("first element of list:-",l[0])
	print("9th element of list:-",l[8])
except ArithmeticError as a:
	print("error",a)
except IndexError as e:
	print("error",e)
s=m+n
print("addition is:-",s)
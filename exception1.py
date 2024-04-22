n=int(input("enter the first number:-"))
m=int(input("enter the second number:-"))
try:
	k=n/m
except ZeroDivisionError as a:
	print("error",a)
s=m+n
print("addition is:-",s)
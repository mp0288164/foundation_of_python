#user define function
def add(x,y):
	z=x+y
	return z
def sub(m,n):
	p=m-n
	return p
#_main_
a=int(input("enter the first no:-"))
b=int(input("enter the second no:-"))
c=add(a,b)
print("sum:-",c)
e=sub(a,b)
print("minus:-",e)
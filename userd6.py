#Function returning multiple values
def calculate(x,y):
	return x+y,x-y,x*y,x/y,x%y
#_main_
a,b,c,d,e=calculate(12,6)
print("addition:-",a)
print("subtraction:-",b)
print("multiplication:-",c)
print("division:-",d)
print("modulodivision;-",e)

a=int(input("enter your purch.amount:-"))
age=int(input("enter the age:-"))
dis=0
if age>16:
	dis=a*10/100
	print("total amount with 10% discount:-",a-dis)
else:
	print("total amount without discount:-")
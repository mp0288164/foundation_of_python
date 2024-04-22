n=int(input("enter the no:-"))
d=0
while n!=0:
	k=n%10
	d=d*10+k
	n=n//10
print("reverse no is:-",d)
n=int(input("enter the no:-"))
k=0
while n>0:
	j=n%10
	k=k*10+j
	n=n//10
print("reverse no is:-",k)
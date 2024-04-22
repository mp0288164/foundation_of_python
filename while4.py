n=int(input("enter the no:-"))
j=0
k=0
while n>0:
	j=n%10
	k=k+j
	n=n//100
print(k)
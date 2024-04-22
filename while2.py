n=int(input("enter any no:-"))
m=0
while n>0:
	j=n%10
	m=m+j
	n=n//10
print("sum of all digits:-",m)
n=int(input("enter the no"))
k=0
for i in range(2,n):
	if n%i==0:
		k==1
		break
if k==0:
	print("no is prime")
else:
	print("no is not prime")
print("prime no. is a divisal by self and 1")
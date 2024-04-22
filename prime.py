
for n in range(1,101):
	k=0
	for i in range(2,n):
		if n%i==0:
			k=1
			break
	if (k==0):
			print("no is prime",n)
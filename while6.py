n= int(input("enter any no:-"))
m=n
k=0
while m>0:
	j=n%10
	k=k+j*j*j
	m=m//10
if n==k:
	print("no. is armstrong")
else:
	print("no. is not armstrong")
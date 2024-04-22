n=int(input("enter the no:-"))
m=n
r=0
while n>0:
	k=n%10
	r=r*10+k
	n=n//10
if (m==r):
	print("no is palindrome")
else:
	print("no is not palindrome")
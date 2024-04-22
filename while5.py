n= int(input("enter any no:-"))
j=n%10
while n>9:
	n=n//10
j+=n
print("sum of first and last digits:-",j)

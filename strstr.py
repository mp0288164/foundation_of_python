str=["i love my india "]
print("string is :-",str)
l=len(str)
for i in range(0,l):
	if i==0:
		k=ord(str[i])
		k=k-32
		str[i]=chr(k)
		print(k)
	elif str[i]==" ": 
		k=ord(str[i+1])
		k=k-32
		str[i+1]=chr(k)
		print(k)
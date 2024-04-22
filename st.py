str="computer"
print("string is :-",str)
for i in range(0,len(str)):
	print(str[i],end="")
print()
for i in range((-len(str)),0,-1):
	print(str[i],end="")
print()
for i in range((len(str)-1),-1,-1):
	print(str[i],end="")
print()
for i in range(-1,len(str),-1):
	print(str[i],end="")
print()
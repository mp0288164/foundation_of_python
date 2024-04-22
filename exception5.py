l=[1,2,3,4,5,6]
try:
	print("list is:-",l)
	print("first element of list:-",l[0])
	print("8th element of list:-",l[7])
except IndexError as e:
	print("error",e)
print("I AMK HERE")
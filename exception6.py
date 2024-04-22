try:
	f=2.0**100
	for i in range(1,100):
		f=f**i
		print(f)
except OverflowError as e:
	print("error:-",e)
print("I AM HERE")
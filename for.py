for i in range(1,6):
	for j in range(5,i-1,-1):
		print(" ",end="")
	for k in range(i,i+j):
		print(k,end="")
	for p in range(k-1,i-1,-1):
		print(p,end="")
	print()
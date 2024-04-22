l1=[2,3,4],[4,5,6],[7,8,9]
print("list is:-",l1)
for i in range(len(l1)):
	for j in range(len(l1[i])):
		print(l1[i][j] ,end="")
	print()
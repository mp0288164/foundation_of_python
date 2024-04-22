list=[12,23,45,67,89,90,90,900,9000,12,34,56,78,123,45,77,98,76,90]
print("list is:-",list)
for i in list:
	if i%3==0 and i%7!=0:
		print("this number is divisal by 3 and not divisal by 7:-",i)
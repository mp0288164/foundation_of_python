l1=[1,2,3,4,5,6,7,0,8,90,190]
print("list is:-",l1)
count=l1[0]
for i in l1:
	if i<=count:
		count=i
print("smallest number in list:-",count)
l1=[1,2,3,4,5,6,7,8,9,10,100]
print("list is :-",l1)
count=0
for i in range(0,len(l1)):
	count+=l1[i]
avg=count%len(l1)
print("sum if all digits in list:-",count)
print("avarage of all digits in list:-",avg)
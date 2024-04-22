n=int(input("how many no do tou want to enter:-"))
list=[]
for i in range(n):
	list.append(int(input("enter the no:-")))
for i in range(n,0,-1):
	for j in range(i-1):
		if list[j]>list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]
print("sorted list is :-")
for i in range(n):
	print(list[i])
s=int(input("enter the no which you want to search:-"))
low=0
high=n-1
while (low<=high):
	mid=(low+high)//2
	if list[mid]==s:
		print("search is successful")
	elif list[mid]>s:
		low=mid-1
	else:
		high=mid+1
else:
	print("search is unsuccessful")  
n=int(input("howw many no do you want to enter"))
itemlist=[]
print("enter the no one by one")
for i in range(n):

	itemlist.append(int(input("enter the no:-")))

s=int(input("enter the no which want you search:-"))
low=0
high=n-1
while(low<=high):
	mid=(low+high)//2
	if  itemlist[mid]==s:
		print("search is successful")
		break
	elif itemlist[mid]>s:
		high=mid-1
	else:
		low=mid+1
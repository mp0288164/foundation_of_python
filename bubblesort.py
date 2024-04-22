n=int(input("howamnyno do you want to enter:-"))
itemlist=[]
for i  in range(n):
	itemlist.append(int(input("enter the number:-")))
for i in range(n,0,-1):
	for j in range(i-1):
		if itemlist[j]>itemlist[j+1]:
			itemlist[j],itemlist[j+1]=itemlist[j+1],itemlist[j]
print("sorted list is:-")
for i in range(n):
	print(itemlist[i])
	
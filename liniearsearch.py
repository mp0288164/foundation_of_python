n=int(input("how many no do you want to enter"))
itemlist=[]
print("print enter no one by one:-")
for i in range (n):
	itemlist.append(int(input("enterno:-")))
s=int(input("enter the no which you search"))
for i in range(n):
	if itemlist[i]==s:
		print("search is successful")
		break
else:
	print("search is not successful")
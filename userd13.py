def feb(x):
	if x==0:
		return 0
	elif x==1:
		return 1
	else:
		return feb(x-1)+(x+2)
#__main__
for i in range(15):
	print(feb(i)," ",end="")
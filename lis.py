l=[1,2,11,22,3,33,4,44,5,55]
for i in range(0,len(l),2):
	l[i],l[i+1]=l[i+1],l[i]
print(l)	


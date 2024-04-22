
n=5
m=0

for i in range(1,101):
	k=0
	for j in range(2,i):
		if i%j==0:
			k=1
			break
	else:
		m+=1
		if m==n:
			print(i)
			break
			
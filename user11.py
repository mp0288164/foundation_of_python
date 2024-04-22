def calculate(**k):
	sum=0
	print(k,type(k))
	for i in k.keys():
		sum+=k[i]
	per=sum/len(k)
	return sum,per
#_main_
s,p=calculate(pyh=90,che=93,math=89,comp=99,eng=97)
print("total marks:-",s)
print("persantage is:-",p)

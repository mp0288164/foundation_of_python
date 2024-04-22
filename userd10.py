def calculate(**k):
	sum=0
	print(k,type(k))
	for i in k.values():
		sum+=i
	per=sum/len(k)
	return sum,per
#_main_
sum,per=calculate(phy=80,math=90,che=89,comp=98,eng=99)
print("total marks:-",sum)
print("persantage is:-",per)

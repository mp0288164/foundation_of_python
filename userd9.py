def calculate(*k):
	sum=0
	for i in k:
		sum+=i
	avg=sum/len(k)
	return sum,avg
#_main_
sum,avg=calculate(10,10,10,10,8,2,4,6)
print("sum of all digits:-",sum)
print("avarage of sum:-",avg)

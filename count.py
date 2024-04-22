str=['apple,'apple','mango','apple','apple','pineple']
print(str)
s=input("choose word in above list for count :-")
count=0
for i in range(0,len(str)):
	if(s==str[i]):
		count+=1
print("total word:-",count)
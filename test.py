inp="xobin^bootcamp"
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vo=['a','e','i','o','u']
t=0
for i in inp:
	for j in range(0,len(al)):
		if i==al[j]:
			t=al[j+1]
			print(t,end="")

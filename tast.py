def print_abc(x):
	for i in range(x+1):
		if(i<10):
			print(i,end="")
			continue
		c=1
		t=1
		d=t%10
		t//=10
		while(t>0):
			if(abs(d-t%10)!=1):
				c=0
				break
			d=t%10
			t//=10
		if(c):
			print(i,end="")
x=105
print_abc(x)
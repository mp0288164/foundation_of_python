inp="xobin^bootcamp"
a=" "
for i in inp:
	if i in ['#','*','^']:
		a=a+i
	else:
		c=ord(i)
		c=c+1
		if chr(c) in ['a','e','i','o','u']:
			c=c-32
			a=a+chr(c)
		else:
			a=a+chr(c)
print(a)
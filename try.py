s="i LOVE My inDIA 458110 "
di=0
al=0
lo=0
up=0
for ch in s:
	if ch.islower():
		lo+=1
	elif ch.isupper():
		up+=1
	elif ch.isdigit():
		di+=1
	else:
		al+=1
print("lower count:-",lo)
print("upper count:-",up)
print("digit count:-",di)
print("alpha count:-",al)
	
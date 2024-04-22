cm=int(input("enter your current month:-"))
cd=int(input("enter your current date:-"))
cy=int(("enter your current year:-"))
bd=int(input("enter your birth date:-"))
bm=int(input("enter your birth month:-"))
by=int(("enter your birth year:-"))
if cm==2andcy==cy%4:
	month=29
elif cm==2andcy%4!=0:
	month=28
elif cm in [ 1,3,5,7,8,10,12]:
	month=31
else:
	month=30
if cd>bd:
	ad=cd-bd
else:
	cd=cd+month
	ad=cd-bd
	cm=cm-1
if cm>bm:
	am=cm-bm
else:
	cm=cm+12
	am=cm-bm
	cy=cy-1
	ay=cy-by
print("your age is:-ad,"/"am,"/",ay)
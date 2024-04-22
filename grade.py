phy=int(input("enter the marks of phy:-"))
che=int(input("enter the marks of che:-"))
maths=int(input("enter the marks of maths:-"))
hindi=int(input("enter the marks of hindi:-"))
eng=int(input("enter the marks of eng:-"))
total=phy+che+maths+hindi+english
pre=total\5.0
if per>85 and per<=99:
	print("pass with A++ Grade" per)
elif per>75 and per<=85:
	print("pass with A+ Grade" per)
elif per>60 and per<=75:
	print("pass with A+Grade"per)
elif per>45 and per<=60:
	print("pass with B Grade"per)
elif per>33 and per<=45:
	print("pass with C Grade"per)
else:
	print("you are Fail")
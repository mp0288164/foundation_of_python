n=int(input("enter the unit:-"))
if n<90:
	print("unit in under 90")
	print("rupees in per unit:-",n*2.7)
elif 90<180:
	print("unit in above 90 and under 180")
	print("rupees in per unit:-",n*4.8)
elif 180<270:
	print("unit in above 180 and under 270")
	print("rupees in per unit:-",n*9.8)
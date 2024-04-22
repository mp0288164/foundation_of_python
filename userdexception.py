#userdefine Exception
class BalanceError(Exception):
	pass
#pass keyword is a no objecct in class
def checkbalance():
	money=12000
	withdraw=6000
	try:
		if(money-withdraw)<2000:

			raise BalanceError("insufficiant balance")
			balance=money-withdraw
			print("reamaining balance is:-",balance)
	except BalanceError as e:
		print("error:-",e)
print("i am here")
#__main__
checkbalance()
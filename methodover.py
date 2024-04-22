class sum:
	def getdata(self,datatype,*mylist):
		if datatype=="int":
			self.answer=0
		elif datatype=="float":
			self.answer=0.0
		else:
			self.answer=" "
		for i in mylist:
			self.answer+=i
		return self.answer
#__main__
p=sum()
print("sum of integer item:-",p.getdata("int",2,3,4,5,6,7,9,90,900,90000))
print("sum of all folat item:-",p.getdata("float",1.2,2.1,3.4,4.5,6.7,8.9))
print("sum of all string item:-","string","my","name,","is","manisha","prajapati")
try:
	dic={"rollno":100,"name":"manisha","class":"mca3"}
	print("Dictionary:-",dic)
	print("name:-",dic["name"])
	print("marks:-",dic["marks"])
except KeyError as e:
	print("error:-",e)
print("I AM HERE")
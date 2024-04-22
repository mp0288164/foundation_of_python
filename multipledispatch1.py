from multipledispatch import dispatch
@dispatch(int,int)
def product(x,y):
	return(x*y)
@dispatch(int,int,int)
def product(m,n,q):
	return(m*n*q)
#__main__
print("answer:-",product(5,4))
print("answer is:-",product(5,6,7))

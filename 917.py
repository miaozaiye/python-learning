L = [1]
L1 = [] 
def yang(n):
	L = [1]
	L1 = []
	for i in range(1,n+1) :
		yield L
		L1 = [1]+[L[x-1]+L[x] for x in range(1,i)]+[1]
		L = L1

		

n = yang(5)
print (next (n))
print (next (n))
print (next (n))
print (next (n))

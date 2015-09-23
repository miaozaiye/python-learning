def anti(x):
	return int(str(x)[::-1])

print (anti(35))
print map(anti,(13,12356,6521,9403))

print sorted(['bob', 'zxx', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#practice

# -*- coding:utf-8-*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print sorted(L,key= lambda x:x[0].lower())

print sorted(L,key= lambda x:x[1], reverse = 1)




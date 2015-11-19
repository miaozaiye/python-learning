import struct

'''
def is_bmp(file):
	try:
		with open(file,'rb') as f:
			s = f.read(30)
			atr = struct.unpack('<ccIIIIIIHH',s)
	    	if atr[0] == b'B' and atr[1] == b'M'
	    	    return atr[2],atr[6],atr[7]
	    	else:
	    		raise BaseException
	    except BaseException:
	    	print (file + 'is not a bmp file')

'''

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print (md5.hexdigest())

db = {}

def register(username,password):
	db[username] = get_md5(password + username + 'the - Salt')

def get_md5(str):

	md5 = hashlib.md5()
	md5.update(str.encode('utf-8'))
	return md5.hexdigest()
	
def login(username,password):
	if username in db:
		print ('用户名存在，准备验证密码')
		if db[username] == get_md5(password + username + 'the - Salt'):
			print ('密码正确，登录成功')
		else: 
			print ('密码错误，请重新输入')
	else:
	    print ('用户名不存在')

register('Jane','janejiang')
login ('Jane','janelu')





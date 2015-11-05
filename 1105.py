import time,threading

'''
def loop():  #define the function for subprocess
	print ('thread %s is running...' % threading.current_thread().name) # show it's the subprocess now
	n = 0
	while n < 5:    # make 5 subprocess
		n = n+1
		print ('thread %s >>> %s' %(threading.current_thread().name,n))
		time.sleep(2)
	print ('thread %s ended.' % threading.current_thread().name,n)
    
print ('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'LoopThread') # set the line for subprocess, and name
t.start()
t.join()
print ('thread %s ended.' % threading.current_thread().name) # show it's the father process now
'''

balance = 0
lock = threading.Lock()

def change_it(n):
	# 先存后取，结果应该为0
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			#放心改
			change_it(n)
		finally:
			#改完了一定要释放锁
			lock.release()
		

t1 = threading.Thread(target = run_thread,args = (5,))
t2 = threading.Thread(target = run_thread,args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print ( balance)
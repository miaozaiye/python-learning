import time,threading

# new loop code:
def loop():  #定义程序
 	print ('thread %s is running...' % threading.current_thread().name) # 打印程序开始
 	n = 0
 	while n<5:   
 		n = n+1
 		print ('thread %s >>> %s' % (threading.current_thread().name,n))
 		time.sleep(1) # 挂起1秒
 	print ('thread %s ended.' % threading.current_thread().name)

print ('thread %s is running...' % threading.current_thread().name) # 打印开始
t = threading.Thread(target = loop, name = 'LoopThread') # 指定线程运行 loop程序，以及线程名
t.start() # 开始
t.join() # 结束
print ( 'thread %s ended.' % threading.current_thread().name) # 打印结束

balance = 0
lock = threading.Lock()

def change_it(n):  # 先存后取，结果应该为0
	global balance
	balance = balance + n 
	#print ('balance is -> ',balance,'args is -> ',n)
	balance = balance - n 
	#print ('balance is -> ',balance,'args is -> ',n)

def run_thread(n):
	for i in range (100000):
		lock.acquire()
		try:
		    change_it(n)
		finally:
			lock.release()

t1 = threading.Thread(target = run_thread,args = (5,))
t2 = threading.Thread(target = run_thread,args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print (balance)

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()






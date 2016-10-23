import threading
import time

def thread_task():
	print('child thread starts')
	time.sleep(10)
	print('child thread ends')


print('main thread starts')
task = threading.Thread(target = thread_task)
task.start()
task.join()
print('main thread ends')
###################################
# File Name : basic_threading_function.py
###################################
#!/usr/bin/python3

import threading

def worker(count):
    print ("name : %s, argument : %s" % (threading.currentThread().getName(), count))


for i in range(5):
    t = threading.Thread(target=worker, name="thread %i" % i, args=(i,))
    t.start()

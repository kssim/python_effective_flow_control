###################################
# File Name : basic_multiprocessing_function_main.py
###################################
#!/usr/bin/python3

import os
import multiprocessing

def worker(count):
    print ("name : %s, argument : %s" % (multiprocessing.current_process().name, count))
    print ("parent pid : %s, pid : %s" % (os.getppid(), os.getpid()))
    print ("")


if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=worker, name="process %i" % i, args=(i,))
        p.start()

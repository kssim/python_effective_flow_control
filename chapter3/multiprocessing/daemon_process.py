###################################
# File Name : daemon_process.py
###################################
#!/usr/bin/python3

import time
import multiprocessing


def daemon():
    print ("Start")
    time.sleep(5)
    print ("Exit")


if __name__ == "__main__":
    d = multiprocessing.Process(name="daemon", target=daemon)
    d.daemon = True

    d.start()
    time.sleep(3)

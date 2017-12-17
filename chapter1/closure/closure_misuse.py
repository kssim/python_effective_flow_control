###################################
# File Name : closure_misuse.py
###################################
#!/usr/bin/python3

import datetime
import time

def logger():
    now = datetime.datetime.now()

    def print_log(msg):
        return ("[%s] %s" % (now, msg))

    return print_log


log = logger()
print (log("Start."))

time.sleep(10)

print (log("After 10 sec."))

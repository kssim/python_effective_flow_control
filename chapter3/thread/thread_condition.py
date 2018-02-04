###################################
# File Name : thread_condition.py
###################################
#!/usr/bin/python3

import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")


def receiver(condition):
    logging.debug("Start receiver")

    with condition:
        logging.debug("Waiting...")
        condition.wait()
        time.sleep(1)
        logging.debug("End")

def sender(condition):
    logging.debug("Start sender")

    with condition:
        logging.debug("Send notify")
        condition.notifyAll()
        logging.debug("End")


condition = threading.Condition()

for i in range(5):
    t = threading.Thread(target=receiver, name="receiver %s" % i, args=(condition,))
    t.start()

sender = threading.Thread(target=sender, name="sender", args=(condition,))

time.sleep(1)
with condition:
    condition.notify(1)

time.sleep(3)
sender.start()

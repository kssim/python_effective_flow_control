###################################
# File Name : basic_coroutine.py
###################################
#!/usr/bin/python3


def coroutine():
    while True:
        msg = yield
        print ("Hello, your input message is '%s'" % msg)


c = coroutine()
next(c)
next(c)
c.send("Test")
c.send("Coroutine")

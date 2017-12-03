###################################
# File Name : nested_function.py
###################################
#!/usr/bin/python3

def greeting(name):

    def add_name():
        return ("Hello %s" % name)

    msg = add_name()
    print (msg)


greeting("python")

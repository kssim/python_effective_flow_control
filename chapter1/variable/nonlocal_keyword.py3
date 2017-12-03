###################################
# File Name : nonlocal_keyword.py3
###################################
#!/usr/bin/python3

def greeting(name):
    greeting_msg = "Hello"

    def add_name():
        nonlocal greeting_msg

        greeting_msg += " "
        return ("%s%s" % (greeting_msg, name))

    msg = add_name()
    print (msg)


greeting("python")

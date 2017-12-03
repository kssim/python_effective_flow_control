###################################
# File Name : global_keyword.py
###################################
#!/usr/bin/python3

msg = "Hello"

def write():
    global msg
    msg += " World"
    print (msg)


print ("=== print msg ===")
print (msg)

print ("=== write function ===")
write()

print ("=== print msg ===")
print (msg)

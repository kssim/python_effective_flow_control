###################################
# File Name : dir_closure.py
###################################
#!/usr/bin/python3


def closure():
    def inner():
        pass

    p = dir(inner())

    print ("=== inner attribute ===")
    print (p)
    return inner


p = dir(closure())

print ("=== attribute ===")
print (p)

###################################
# File Name : decorator_basic.py
###################################
#!/usr/bin/python3

def decorator_func(func):
    def wrapper_func():
        print ("before")
        ret = func()
        print ("after")
        return ret
    return wrapper_func

@decorator_func
def base_func():
    print ("base function")


print ("=== Run decorator ===")
base_func()

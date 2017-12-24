###################################
# File Name : unroll_decorator_basic_1.py
###################################
#!/usr/bin/python3

def decorator_func(func):
    def wrapper_func():
        print ("before")
        ret = func()
        print ("after")
        return ret
    return wrapper_func

def base_func():
    print ("base function")


print ("=== Run decorator ===")
decorator_func(base_func)()

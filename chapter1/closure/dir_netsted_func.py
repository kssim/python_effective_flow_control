###################################
# File Name : dir_nested_func.py
###################################
#!/usr/bin/python3


def nested_func():
    def inner():
        pass

    p = dir(inner())

    print ("=== inner attribute ===")
    print (p)


p = dir(nested_func())

print ("=== attribute ===")
print (p)

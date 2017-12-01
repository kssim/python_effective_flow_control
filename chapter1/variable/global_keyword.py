###################################
# File Name : global_keyword.py
###################################
#!/usr/bin/python3

global_var = "global"

def write_test():
    global global_var

    local_var = "local"
    global_var = "is global?"

    print (local_var)
    print (global_var)


def read_test():
    print (global_var)


print ("=== variable ===")
print (global_var)

print ("=== write test ===")
write_test()

print ("=== read test ===")
read_test()

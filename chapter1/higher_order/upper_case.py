###################################
# File Name : upper_case.py
###################################
#!/usr/bin/python3

LOWER_LIST = ["python", "python2", "python3"]
UPPER_LIST = []

def upper_func():
    for data in LOWER_LIST:
        UPPER_LIST.append(data.upper())


print ("=== print result ===")
upper_func()
print (LOWER_LIST)
print (UPPER_LIST)

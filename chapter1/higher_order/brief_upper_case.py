###################################
# File Name : brief_upper_case.py
###################################
#!/usr/bin/python3

LOWER_LIST = ["python", "python2", "python3"]
UPPER_LIST = []

def upper_func(data):
    return data.upper()


print ("=== print result ===")
UPPER_LIST = map(upper_func, LOWER_LIST)
print (LOWER_LIST)
print (list(UPPER_LIST))

###################################
# File Name : return_yield.py
###################################
#!/usr/bin/python3

def gen():
    yield 1
    yield 2
    yield 3

def normal():
    return 1
    return 2
    return 3


print ("=== print gen function ===")
print (gen())

print ("=== print normal function===")
print (normal())

print ("=== print gen function in loop ===")
for g in gen():
    print (g)

print ("=== print normal function in loop ===")
for n in normal():
    print (n)

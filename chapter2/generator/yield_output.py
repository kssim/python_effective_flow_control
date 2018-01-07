###################################
# File Name : yield_output.py
###################################
#!/usr/bin/python3

def generator():
    yield 1
    yield 2
    yield 3

def normal():
    return 1
    return 2
    return 3


print ("=== print generator ===")
print (generator())

print ("=== print normal ===")
print (normal())

print ("=== print generator in loop ===")
for gf in generator():
    print (gf)

print ("=== print normal in loop ===")
for nf in normal():
    print (nf)

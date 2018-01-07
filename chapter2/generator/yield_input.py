###################################
# File Name : yield_input.py
###################################
#!/usr/bin/python3

def gen():
    exponent = 2

    while True:
        exponent = 2 ** (yield exponent)


print ("=== print gen function ===")
g = gen()

print (next(g))
print (g.send(3))
print (g.send(5))

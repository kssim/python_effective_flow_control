###################################
# File Name : calculator_2.py
###################################
#!/usr/bin/python3

def calculator(x):

    def add(y):
        return x+y

    return add


print ("=== print calculation ===")
f = calculator(10)
print (f(5))
print (f(10))

###################################
# File Name : higher_order_function.py
###################################
#!/usr/bin/python3

def multiple_of_ten(f):
    square_root = 10
    return lambda x: f(square_root, x)

def square(square_root, x):
    return square_root ** x


print ("=== print result ===")
f = multiple_of_ten(square)
print (f(2))
print (f(3))

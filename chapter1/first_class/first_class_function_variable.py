###################################
# File Name : first_class_function_variable.py
###################################
#!/usr/bin/python3

def square(x):
    return x*x


print ("Function call")
print (square(10))

print ("Assign variable")
f = square
print (f(10))

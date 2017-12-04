###################################
# File Name : first_class_function_paramter.py
###################################
#!/usr/bin/python3

def square(x):
    return x*x

def bind(func, arg_list):
    result = []
    for arg in arg_list:
        result.append(func(arg))
    return result


arg_list = [5, 10]
print ("Assign variable & send parameter")
squares = bind(square, arg_list)
print (squares)

###################################
# File Name : range.py3
###################################
#!/usr/bin/python3

import sys

def get_type_and_size(value):
	print ("type : %s" % type(value))
	print ("size : %d" % sys.getsizeof(value))


print ("=== Range size : 10 ===")
get_type_and_size(range(10))

print ("=== Range size : 100 ===")
get_type_and_size(range(100))

print ("=== Xrange size : 10 ===")
get_type_and_size(xrange(10))

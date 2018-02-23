###################################
# File Name : yield_from.py (Python 3.3 or later)
###################################
#!/usr/bin/python3


def new():
	yield from range(10)

def old():
	for item in range(10):
		yield item


print ("== yield ==")
print (list(old()))

print ("== yield from ==")
print (list(new()))

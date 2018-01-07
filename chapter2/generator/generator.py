###################################
# File Name : generator.py
###################################
#!/usr/bin/python3

def generator(items):
    count = 0

    for item in items:
        if count == 10:
            return item

        count += 1
        yield item


print ("=== print generator ===")
for i in generator(range(15)):
    print (i)

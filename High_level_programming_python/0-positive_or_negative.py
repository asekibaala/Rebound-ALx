#!/usr/bin/python3
import random
num = random.randint(-100,100)
if num >0:
    print("{:d} is postive".format(num))
elif num == 0:
    print("{:d} is Zero".format(num))
else:
    print("{:d} is negative".format(num))
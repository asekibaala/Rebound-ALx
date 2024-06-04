#!/usr/bin/python3
import random
num = random.randit(-10,10)
if num >0:
    print("{:d} is postive".format(num))
elif num == 0:
    print("{:d} is Zero".format(num))
else:
    print("{:d} is negative".format(num))
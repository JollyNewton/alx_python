#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number>0):
    print(end="{} is positive".format(number))
if (number==6):
    print(end="{} is zero" .format(number))
if (number<0):
    print(end="{} is negative".format(number))

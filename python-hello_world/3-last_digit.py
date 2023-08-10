#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number%10>5):
    print("Last Digit of",end=" ")
    print(number,end=" is ")
    print(number%10,end=" and is less than 5")
if (number%10<6 and number%10!=0):
    print("Last Digit of",end=" ")
    print(number,end=" is ")
    print(number%10,end=" and is less than 6 and not 0")
if (number%10==0):
    print("Last Digit of",end=" ")
    print(number,end=" is ")
    print(number%10,end=" and is 0")

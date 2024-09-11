import math
import os
import random
import re
import sys


def freqSort(element):
    return (-element[1], element[0])

if __name__ == '__main__':

    dict = {}
    s = input()
    count = 0

    for char in s:
        if char in dict:
            dict[char]+=1
        else: dict[char]=1

    yay= sorted(dict.items(), key=freqSort)
    
    cnt = 0

    for x in yay:
        print(x[0],x[1])
        cnt+= 1
        if cnt==3: break
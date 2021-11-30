# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:23:09 2021

@author: mered
"""
import math



m = input("Enter any positive integer: ")
n = int(m)
expvector = [0]*n
numvector = [0]*n
fivepowers = math.floor(math.log(n)/math.log(5))
numzeros = 0
for i in range(1,n+1):
    expvector[i-1]=n+1-i
    numvector[i-1]=i
for i in range(1,n+1):
    for k in range(1,fivepowers+1):
        if numvector[i-1]%(5**k)==0:
          numzeros+=(expvector[i-1])
print(numzeros)
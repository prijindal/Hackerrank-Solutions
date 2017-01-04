#!/bin/python3

import sys


n = int(input().strip())

a = 0

while(n>0):
    a = a*10 + n%2
    n = int(n/2)

ans = 0
max = 0
for i in str(a):
    if i == '1':
        max+=1
    else:
        if (max > ans):
            ans = max
        max = 0

if (max >= ans):
    ans = max

print(ans)

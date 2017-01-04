#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

jumpDiff = v1 - v2
initDiff = x1 - x2

if jumpDiff == 0:
    print("NO")
elif initDiff%jumpDiff == 0:
    if initDiff > 0 and jumpDiff < 0:
        print("YES")
    elif initDiff < 0 and jumpDiff > 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

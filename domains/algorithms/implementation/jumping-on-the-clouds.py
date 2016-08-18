#!/bin/python3

import sys


n = int(input().strip())
C = [int(c_temp) for c_temp in input().strip().split(' ')]


cur = 0
i = 0
while i < n:
    if cur + 2 < n and C[cur+2] == 1:
        cur+=1
    elif cur == n - 2:
        cur+=1
    else:
        cur+=2
    # print(cur, i)
    if cur >= n:
        break;
    else:
        i+=1
print(i)

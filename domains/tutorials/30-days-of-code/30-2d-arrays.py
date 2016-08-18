#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

sum = -1000
for i in range(1,5):
    for j in range(1,5):
        s = arr[i][j]
        s += arr[i-1][j-1]
        s += arr[i-1][j]
        s += arr[i-1][j+1]
        s += arr[i+1][j-1]
        s += arr[i+1][j]
        s += arr[i+1][j+1]
        if (s > sum):
        	sum = s

print(sum)

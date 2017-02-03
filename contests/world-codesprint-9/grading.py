#!/bin/python
n = input();

A = [input() for i in xrange(n)]

for i in xrange(n):
    if A[i] < 38:
        continue;
    else:
        if (A[i] + 1)%5 == 0:
            A[i] += 1
        elif (A[i] + 2)%5 == 0:
            A[i] += 2

for i in A:
    print(i)

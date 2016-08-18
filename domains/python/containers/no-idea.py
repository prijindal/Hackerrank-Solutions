# TIMEOUT
n = input()
N = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

sum = 0
for i in A:
    if i in N:
        sum+=1

for i in B:
    if i in N:
        sum-=1

print(sum)

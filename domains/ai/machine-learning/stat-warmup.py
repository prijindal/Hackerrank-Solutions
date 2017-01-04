from math import sqrt

def roundUp(N):
    return round(N*10)/10

N = int(input())

A = [int(x) for x in input().split()]

print(len(A))
A.sort()

dict = {}

sum = 0

median = 0
if N%2 == 0:
    mid = int(N/2)
    print(mid)
    print(len(A))
    median = A[mid] + A[mid - 1]
    median = median/2
else:
    median = A[(N-1)/2]

for i in A:
    sum+=i
    dict[i] = 0

mean = sum/N

for i in A:
    dict[i]+=1

high = 0
mode = 9999999999999
for i in A:
    if dict[i] >= high and i <= mode:
        high = dict[i]
        mode = i

standardSum = 0
for i in A:
    standardSum+=(i - mean)*(i - mean)

sd = sqrt(standardSum/N)

sigmaM = sd/sqrt(N)

conA, conB = [mean - 1.96*sigmaM, mean + 1.96*sigmaM]

print(roundUp(mean))
print(roundUp(median))
print(mode)
print(roundUp(sd))
print('{} {}'.format(roundUp(conA), roundUp(conB)))

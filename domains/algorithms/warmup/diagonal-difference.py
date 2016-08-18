n = int(raw_input())

N = [[int(i) for i in raw_input().split(' ')] for j in range(n)]

sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i==j:
            #print(i,j, '1')
            sum1+=N[i][j]
        if i+j==n-1:
            #print(i,j, '2')
            sum2+=N[i][j]

print abs(sum2-sum1)

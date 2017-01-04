n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

count = 0

for i in range(0, n):
    for j in range(i + 1, n):
        if (a[i] + a[j])%k==0:
            count+=1

print(count)

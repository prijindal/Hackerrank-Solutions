n = int(input())

a = [int(x) for x in input().split()]

minimum = n + 1

for i in range(0, n):
    for j in range(i + 1, n):
        k = abs(i - j)
        if (a[i] == a[j]) and k < minimum:
            minimum = k

if minimum == n + 1:
    minimum = -1
print(minimum)

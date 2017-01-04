a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

A = 0
B = 0

for i in range(3):
    if a[i] > b[i]:
        A += 1
    elif a[i] < b[i]:
        B += 1

print(A, B)

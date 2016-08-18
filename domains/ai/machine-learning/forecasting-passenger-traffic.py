F = []

N = int(input())

for i in range(N):
    M, passengers = input().split()
    passengers = int(passengers)
    F.append(passengers)

k = 0
i = 0

while k < 12:
    i = k
    j = 0
    sum = 0
    while i < N:
        sum+=F[i]
        i+=12
        j+=1
    k+=1
    print(int(sum/j))

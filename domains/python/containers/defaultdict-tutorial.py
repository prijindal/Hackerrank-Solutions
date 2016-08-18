n,m = (int(i) for i in input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

for i in B:
    k = 0
    found = False
    for j in A:
        k+=1
        if i==j:
            found = True
            print(k, end=' ')
    if not found:
        print(-1)
    else:
        print('')

INF = 9999

N,M = [int(x) for x in input().split()]

G = [[INF for i in range(0, N)] for j in range(0, N)]

for i in range(0, M):
    x,y,r = [int(x) for x in input().split()]
    G[x-1][y-1] = r

dist = G

for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

T = int(input())
for i in range(0, T):
    a,b = [int(x) for x in input().split()]
    s = dist[a-1][b-1]
    if s == INF:
        print(-1)
    else:
        print(s)

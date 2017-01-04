INF = 9999999

def bfSearch(Graph, n, root):
    distance = [INF for i in range(n)]
    parents = [None for i in range(n)]

    Q = []

    distance[root] = 0
    Q.append(root)

    while len(Q) > 0:
        current = Q.pop()
        for j in range(n):
            for k in range(n):
                # print(j, k, G[j][k], current)
                if j == current:
                    if Graph[j][k] == 1:
                        if distance[k] == INF:
                            distance[k] = distance[current] + 1
                            parents[k] = current
                            Q.append(k)
                        # K is adjacent to current
                elif k == current:
                    if Graph[j][k] == 1:
                        if distance[j] == INF:
                            distance[j] = distance[current] + 1
                            parents[j] = current
                            Q.append(j)
                        # j is adjacent to current

    out = ''
    for i in distance:
        if i == 0:
            pass
        elif i != INF:
            out += '{} '.format(i*6)
        else:
            out += '-1 '
    print(out)
q = int(input())

for i in range(q):
    N,M = [int(x) for x in input().split()]

    G = [[0 for i in range(0, N)] for j in range(0, N)]

    for i in range(0, M):
        x,y = [int(a) for a in input().split()]
        G[x-1][y-1] = 1
    s = int(input()) - 1
    bfSearch(G, N, s)

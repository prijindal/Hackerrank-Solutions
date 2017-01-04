import collections
n = int(input())

L = [input() for _ in range(n)]

Occ = collections.OrderedDict()

for i in range(n):
    Occ[L[i]] = 0

for i in range(n):
    Occ[L[i]]=Occ[L[i]]+1

print(len(Occ))
i = 0

for i in Occ:
    print(Occ[i], end=' ')

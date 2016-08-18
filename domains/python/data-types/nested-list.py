n=int(raw_input())
L=[]

for i in xrange(n):
    L.append([raw_input(),float(raw_input())])

first=100
for i in xrange(n):
    if L[i][1] < first:
        first=L[i][1]
second=100
for i in xrange(n):
    if L[i][1] >first and L[i][1] <second:
        second=L[i][1]

ans=[]
for i in L:
    if i[1] == second:
        ans.append(i[0])
ans.sort()
for i in ans:
    print i

A = [int(i) for i in raw_input().split(' ')]

l = len(A)

for i in xrange(l):
    for j in xrange(i):
        if A[i] < A[j]:
            A[i],A[j] = A[j],A[i]

print('{0} {1}'.format(sum(A[:(l - 1)]), sum(A[1:])))

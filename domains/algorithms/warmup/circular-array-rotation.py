n, k, q = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]

B = [0 for i in range(0, n)]

for i in range(0,n):
	newPos = i + k
	newPos = newPos%n
	# print(newPos)
	B[newPos] = A[i]

# print(B)

for i in range(q):
	print(B[int(input())])
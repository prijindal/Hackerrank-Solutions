def findLeast(B, W, X, Y, Z):
    blackCost = min(X, Y+Z)
    whiteCost = min(Y, X+Z)
    return B*blackCost + W*whiteCost

t = int(input())

answer = []
for i in range(t):
    b, w = [int(i) for i in input().split()]
    x, y, z = [int(i) for i in input().split()]
    answer.append(findLeast(b, w, x, y, z))

for i in answer:
    print(i)

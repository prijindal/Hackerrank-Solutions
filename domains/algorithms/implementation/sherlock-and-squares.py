import math
def checkSquares(a, b):
    A = math.floor(math.sqrt(a))
    B = math.floor(math.sqrt(b))
    ans = B - A

    if A*A == a:
        ans+=1

    return ans

t = int(input())

L = [input() for i in range(t)]

for i in L:
    m, n = i.split(' ')
    print(checkSquares(int(m), int(n)))

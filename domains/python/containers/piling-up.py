def findMin(list):
    maxPos = 0
    for i in range(len(list)):
        if list[maxPos] > list[i]:
            maxPos = i
    return maxPos

def checkIncreasing(list):
    for i in range(1,len(list)):
        if list[i-1] > list[i]:
            return False
    return True

def checkDecreasing(list):
    for i in range(1,len(list)):
        if list[i-1] < list[i]:
            return False
    return True

def checkList(list):
    min = findMin(list)
    A = list[:min]
    B = list[min:]
    return checkIncreasing(B) and checkDecreasing(A)

t = int(input())
ans = []

for i in range(t):
    n = int(input())
    L = [int(i) for i in input().split()]
    ans.append(checkList(L))

for a in ans:
    print('Yes' if a else 'No')

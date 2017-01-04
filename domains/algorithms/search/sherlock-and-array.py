def findMiddle(array):
    if len(array) == 1:
        return 'YES'
    sumLeft = 0
    sumRight = sum(array[1:])
    for i in range(1,len(array)):
        sumLeft += array[i-1]
        sumRight -=array[i]
        if sumLeft == sumRight:
            return 'YES'
    return 'NO'

t = int(input())
answers = []

for i in range(t):
    n = int(input())
    L = [int(i) for i in input().split(' ')]
    answers.append(findMiddle(L))

for i in answers:
    print(i)

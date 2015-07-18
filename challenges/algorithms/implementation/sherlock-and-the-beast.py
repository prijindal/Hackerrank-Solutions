def findMaxFive(n):
    # Find maximum number with all digits 5 if 3-digit like number
    return '5'*n

def findMaxThree(n):
    return '3'*n
    # Find maximum number with all digits 3 if 5-digit like numbe

def restCases(n):
    s = 0
    found = False
    maxS = 0
    ansM = 0
    while s < n:
        s+=3
        m = n-s
        if m%5==0:
            found = True
            maxS = s
            ansM = m
        else:
            continue
    if found:
        return '5'*maxS+'3'*ansM
    else:
        return -1
    #'5'*s+'3'*m # s is multiple of 3, m is multiple of 5 and s+m=n

def solveNumber(num):
    answers = []
    if num%5 == 0:
        answers.append(int(findMaxThree(num)))
    if num%3 == 0:
        answers.append(int(findMaxFive(num)))

    answers.append(int(restCases(num)))
    return max(answers)

t = int(input())

L = [int(input()) for _ in range(t)]

for i in L:
    print(solveNumber(i))

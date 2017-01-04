def checkString(message):
    count = 0
    L = list(message)
    i = 1
    while i < len(L):
        if L[i] == L[i-1]:
            del L[i]
            count+=1
        else:
            i+=1
    return count

t = int(input())
messagelist = [input() for i in range(t)]

for i in messagelist:
    print(checkString(i))

#Wrong Answer
def findLex(message):
    messList = list(message)
    for i in range(len(messList)-1,0 ,-1):
        for j in range(i,-1,-1):
            if messList[i] > messList[j]:
                messList[i], messList[j] = messList[j], messList[i]
                return messList[:j+1]+sorted(messList[j+1:])
    if messList == list(message):
        return 'no answer'
    else:
        return messList

t = int(input())

L = [input() for _ in range(t)]

for i in L:
    print(''.join(findLex(i)))

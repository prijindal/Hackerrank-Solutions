def solution(listOfPeople):
    # This list has all the people along with a set of all the topics they know
    max = 0
    for i in range(0, len(listOfPeople)):
        for j in range(i, len(listOfPeople)):
            temp = listOfPeople[i] | listOfPeople[j]
            if len(temp) > max:
                max = len(temp)

    count = 0
    for i in range(0, len(listOfPeople)):
        for j in range(i, len(listOfPeople)):
            temp = listOfPeople[i] | listOfPeople[j]
            if len(temp) == max:
                count+=1

    print(max)
    print(count)

n, m =[int(i) for i in input().split()]

L = [input() for i in range(n)]

list = []
for s in L:
    tempList = set()
    for k in range(m):
        if s[k] == '1':
            tempList.add(k)
    list.append(tempList)

solution(list)

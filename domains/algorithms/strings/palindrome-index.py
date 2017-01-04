# TimeOut
class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


d = Deque()

def isPalindrom(string):
    for ch in string:
        d.addFront(ch)

    stillSame = True
    while d.size() > 1 and stillSame:
        if d.removeRear() != d.removeFront():
            stillSame = False

    return stillSame

def findIndex(message):

    if isPalindrom(message):
        return -1

    for i in range(len(message)):
        if isPalindrom(message[0:i]+message[i+1:]):
            return i
    return -1

t = int(input())
L = [input() for _ in range(t)]

for i in L:
    print(findIndex(i))

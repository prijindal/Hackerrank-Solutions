class Ladder(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Snake(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class Board(object):
    def __init__(self, ladders, snakes, probabilities):
        self.ladders = ladders
        self.snakes = snakes
        self.probabilities = probabilities
        self.win = False
        self.curPos = 0

    def move(self):
        a = self.__rollDice()
        self.curPos += a
        if self.curPos == 100:
            self.win = True
        elif self.curPos > 100:
            self.curPos -= a
            return;
        # curPos = 55
        for i in self.ladders:
            if i.start == self.curPos:
                self.curPos = i.end
        for i in self.snakes:
            if i.head == self.curPos:
                self.curPos = i.tail
        return self.curPos

    def __rollDice(self):
        r = random()
        sumP = 0
        k = 1
        while k <= 6:
            sumP += self.probabilities[k - 1]
            if r < sumP:
                return k
            else:
                k+=1
        return 6


from random import random

def game(snakes, ladders, p):
    B = Board(snakes, ladders, p)
    k = 0
    while B.win == False:
        B.move()
        k+=1
    return k

def simulate():
    P = [float(x) for x in input().split(',')]
    nL, nS = [int(x) for x in input().split(',')]

    L = []
    S = []

    lInput = [x for x in input().split()]
    sInput = [x for x in input().split()]

    for i in lInput:
        s, e = [int(x) for x in i.split(',')]
        l = Ladder(s, e)
        L.append(l)

    for i in sInput:
        h, t = [int(x) for x in i.split(',')]
        s = Snake(h, t)
        S.append(s)

    sum = 0
    for i in range(5000):
        sum += game(L, S, P)
    print(int(sum/5000))
    # break;

t = int(input())
#
for i in range(t):
    simulate()

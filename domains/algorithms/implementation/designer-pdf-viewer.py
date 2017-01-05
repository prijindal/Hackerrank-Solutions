HEIGHT = [int(i) for i in raw_input().split(' ')]

inputString = list(raw_input())

maxHeight = 0

for c in inputString:
    c = ord(c) - 97
    if HEIGHT[c] > maxHeight:
        maxHeight = HEIGHT[c]

print(maxHeight * len(inputString))

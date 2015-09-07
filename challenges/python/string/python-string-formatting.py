def getString(num, base=10):
    CHARS = '0123456789ABCDEF'
    if num//base==0:
        return CHARS[num%base]
    else:
        return getString(num//base, base) + CHARS[num%base]

def printFormatted(S, width):
    l = len(S)
    print(' '*(width-l) + S + ' ', end='')

N = int(input())
max_width = len(str(getString(N, 2)))
BASES = [10, 8, 16, 2]

for i in range(1, N+1):
    for j in BASES:
        printFormatted(getString(i, j), max_width)
    print()

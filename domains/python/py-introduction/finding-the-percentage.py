t=int(input())

L=[input() for i in range(t)]
M = {}
for i in range(t):
    stri = L[i].split()
    M[stri[0]]={'one': float(stri[1]), 'two': float(stri[2]), 'three': float(stri[3])}

s = input()
if s in M:
    sumMarks = (M[s]['one'] + M[s]['two'] + M[s]['three'])
    print('%.2f' %(float(sumMarks)/3))

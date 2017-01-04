n = int(input())
s = input()
k = int(input())
U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
L = 'abcdefghijklmnopqrstuvwxyz'*2

l = []
for i in s:
    if i in U:
        l.append(U[k+ord(i)-65])
    elif i in L:
        l.append(L[k+ord(i)-97])
    else:
        l.append(i)

print(''.join(l))

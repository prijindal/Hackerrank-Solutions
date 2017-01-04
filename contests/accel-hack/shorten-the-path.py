# Enter your code here. Read input from STDIN. Print output to STDOUT
N = 0
S = 0
E = 0
W = 0

I = input().lower()
for i in I:
    if i == 'n':
        N+=1
    elif i == 's':
        S+=1
    elif i == 'e':
        E+=1
    elif i == 'w':
        W+=1

hor = E - W
if hor > 0:
    print('E'*hor,end='')
elif hor < 0:
    print('W'*(-hor),end='')

vert = N - S
if vert > 0:
    print('N'*vert,end='')
elif vert < 0:
    print('S'*(-vert),end='')

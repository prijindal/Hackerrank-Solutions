X,Y,Z,N = [int(raw_input()) for i in xrange(4)]

L=[]
for x in range(0,X+1):
    for y in range(0,Y+1):
        for z in range(0,Z+1):
            if x+y+z!=N:
                L.append([x,y,z])

L.sort()

print L

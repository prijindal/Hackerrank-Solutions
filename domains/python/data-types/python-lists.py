n=int(raw_input())

L=[]

i=0
while i < n:
    inp = raw_input().split()

    if inp[0]=="append":
        inp[1]=int(inp[1])
        L.append(inp[1])
    elif inp[0]=="extend":
        inp[1]=int(inp[1])
        L.extend(inp[1])
    elif inp[0]=="insert":
        inp[1]=int(inp[1])
        inp[2]=int(inp[2])
        L.insert(inp[1],inp[2])
    elif inp[0]=="remove":
        inp[1]=int(inp[1])
        L.remove(inp[1])
    elif inp[0]=="pop":
        L.pop()
    elif inp[0]=="index":
        inp[1]=int(inp[1])
        L.index(inp[1])
    elif inp[0]=="count":
        inp[1]=int(inp[1])
        L.count(inp[1])
    elif inp[0]=="sort":
        L.sort()
    elif inp[0]=="reverse":
        L.reverse()
    if inp[0]=="print":
        print L

    i+=1

    

N,J = [int(i) for i in raw_input().split(' ')]
A = [int(i) for i in raw_input().split(' ')]

k = True # Skip possible
j = 0
for i in A:
    if J >= i:
        j+=1
        continue
    elif J < i and k==True:
        # print(j)
        k = False
        continue
    else:
        break
print(j)

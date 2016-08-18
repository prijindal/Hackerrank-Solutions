n = int(input())
N = [int(i) for i in input().split()]

pos = 0.0
neg = 0.0
zero = 0.0
for i in N:
    if i > 0:
        pos+=1
    elif i < 0:
        neg+=1
    else:
        zero+=1
total = pos+neg+zero
print("%.3f"% (pos/total))
print("%.3f"% (neg/total))
print("%.3f"% (zero/total)) 

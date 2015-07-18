n=int(raw_input())

L=[int(i) for i in raw_input().split()]

first=max(L)
ans=-100000

for i in L:
    if i<first and i>ans:
        ans=i
print ans

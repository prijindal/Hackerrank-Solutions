m=int(raw_input())
M=[int(i) for i in raw_input().split()]

n=int(raw_input())
N=[int(i) for i in raw_input().split()]

ans=[]
for i in M:
	available=True
	for j in N:
		if i==j:
			available=False
	if available and i not in ans:
		ans.append(i)


for i in N:
	available=True
	for j in M:
		if i==j:
			available=False
	if available and i not in ans:
		ans.append(i)

ans.sort()
for i in ans:
	print i

n=int(raw_input())

NUM=[raw_input() for i in xrange(n)]

ans=[]
for n in NUM:
	if len(n)!=10:
		ans.append('NO')
	elif n.isdigit() == False:
		ans.append('NO')
	elif n[0] not in ['7','8','9']:
		ans.append('NO')
	else:
		ans.append('YES')

for i in ans:
	print i

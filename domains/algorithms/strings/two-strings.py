def strings(a,b):
	M=[[0 for i in xrange(26)] for j in xrange(2)]


	for i in a:
		M[0][ord(i)-97]+=1

	for i in b:
		M[1][ord(i)-97]+=1

	ans=False
	for i in xrange(26):
		if (M[0][i]>0) and (M[1][i]>0):
			ans = True
			break

	return ans

t=int(raw_input())
ANS=[0 for i in xrange(t)]

for i in xrange(t):
	a=raw_input()
	b=raw_input()

	if strings(a,b):
		ANS[i]="YES"
	else:
		ANS[i]="NO"

for i in xrange(t):
	print ANS[i]

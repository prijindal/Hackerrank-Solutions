M=[[0 for i in xrange(26)] for j in xrange(2)]

a=raw_input()
b=raw_input()

for i in a:
	M[0][ord(i)-97]+=1

for i in b:
	M[1][ord(i)-97]+=1

ans=0
for i in xrange(26):
	ans+=abs(M[0][i]-M[1][i])

print ans

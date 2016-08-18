def anagram(a,b):
	M=[[0 for i in xrange(26)] for j in xrange(2)]


	for i in a:
		M[0][ord(i)-97]+=1

	for i in b:
		M[1][ord(i)-97]+=1

	ans=0
	for i in xrange(26):
		if(M[1][i]-M[0][i]) >0 :
			ans+=M[1][i]-M[0][i]

	return ans


def split_anagram(s):
	n=len(s)
	if n%2==0:
		return anagram(s[:n/2],s[n/2:])
	else:
		return -1

t=int(raw_input())
inp=[raw_input() for j in xrange(t)]

for j in xrange(t):
	print split_anagram(inp[j])

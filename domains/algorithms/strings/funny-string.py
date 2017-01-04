def check_funny(s):
	r=s[::-1]
	n=len(s)
	result=True
	for i in range(1,n):
		a=abs(ord(s[i])-ord(s[i-1]))
		b=abs(ord(r[i])-ord(r[i-1]))
		if(a!=b):
			result=False;

	return result

t=int(raw_input())
ans=[False for j in xrange(t)]

for j in xrange(t):
	ans[j]=check_funny(raw_input())

for j in xrange(t):
	print "Funny" if ans[j] else "Not Funny"

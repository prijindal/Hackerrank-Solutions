pi=3.1415926535897932384626433833

t=int(raw_input())
ans=[0 for i in xrange(t)]

for i in xrange(t):
	value=0
	k=0
	s=raw_input();
	a=s.split();
	pow_length=pow(10,len(a)-1)
	pi_value=int(pi*pow_length)
	pi_value=float(pi_value)
	for j in a:
		n=len(j)
		value+=n*pow(10,-k)
		k+=1
	value=value*pow_length
	ans[i]=abs(value-pi_value)

for i in xrange(t):
	if ans[i]<0.01:
		print "It's a pi song.";
	else:
		print "It's not a pi song.";

t=int(raw_input())
n=[int(raw_input()) for i in xrange(t)]

for i in xrange(t):
	a=n[i]
	sum=0
	b=0
	while a!=0:
		b=a%10
		a=a/10
		if b!=0:
			if n[i]%b==0 :
				sum+=1

	print sum

def check_kaprekar(n):
	if n==1:
		return True
	elif n<4:
		return False
	s=str(n)
	l=len(s)
	square=n*n
	sqrstr=str(square)
	a=int(sqrstr[0:len(sqrstr)-l])
	b=int(sqrstr[len(sqrstr)-l:])

	if a+b==n:
		return True
	else:
		return False

i=int(raw_input())

j=int(raw_input())
found=False;
for k in range(i,j+1):
	if check_kaprekar(k):
		found=True
		print k,

if found==False:
	print "INVALID RANGE"

n=int(raw_input())

L=[raw_input() for i in xrange(n)]

numb=[]
for j in L:
	if j[0]=='0' and len(j)==11:
		numb.append(j[1:])
	elif j[0:2]=='91' and len(j)==12:
		numb.append(j[2:])
	elif j[0:3]=='+91' and len(j)==13:
		numb.append(j[3:])
	elif len(j)==10:
		numb.append(j)

numb.sort()
for i in numb:
	print "+91",i[:5],i[5:]

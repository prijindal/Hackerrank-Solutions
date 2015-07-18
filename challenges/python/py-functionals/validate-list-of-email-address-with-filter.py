def valid_found(s):
	vat=0
	vdot=0
	for j in s:
		if j=='@':
			vat+=1
		elif j=='.':
			vdot+=1
	if vat==1 and vdot==1:
		return True
	else:
		return False

n=int(raw_input())
L=[raw_input() for i in xrange(n)]

ans=[]
for i in xrange(n):

	if valid_found(L[i]) == True:
		A=L[i].split('@')
		A[1]=A[1].split('.')
		B=[A[0],A[1][0],A[1][1]]
		valid = True
		for j in B[0]:
			if (j.isalnum() == True or j=='_' or j=='-') == False:
				valid=False
		if len(B[0])==0:
			valid=False
		if B[1].isalnum()==False:
			valid=False
		if len(B[2])>3:
			valid=False

	else:
		valid=False
	if valid :
		ans.append(L[i])

ans.sort()
print ans

import sys
n=int(raw_input())
b=[[0 for i in xrange(n)] for i in xrange(n)]
for i in range(0,n):
    a=long(raw_input())
    j=n-1
    while a!=0:
        b[i][j]=int(a%10)
        a=a/10
        j-=1
#print b
for i in range(1,n-1):
    for j in range(1,n-1):
        if b[i+1][j]<b[i][j] and b[i-1][j]<b[i][j] and b[i][j+1]<b[i][j] and b[i][j-1]<b[i][j]:
            b[i][j]='X'
for i in range(0,n):
    for j in range(0,n):
		if b[i][j]!='X':
			#print "\b%r"%(b[i][j]),
			sys.stdout.write(str(b[i][j]))
		else:
			#print "\b%c"%(b[i][j])
			sys.stdout.write(b[i][j])
    print ""

n=int(raw_input())
a=raw_input().split(' ')
#print a
p=int(a[0])
x=[]
y=[]
for i in range(1,n):
	k=int(a[i])
	if p>k:
		x.append(k)
	else :
		y.append(k)
if len(x)>0:
	print " ".join([str(i) for i in x]),
print p,
if len(y)>0:
	print " ".join([str(i) for i in y]),

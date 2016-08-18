def print_c(l):
	if l[0] !=0 and l[1] !=0:
		print "%.2f %s %.2fi" %(l[0],"-" if l[1]<0 else "+",abs(l[1]))
	elif l[0] !=0:
		print "%.2f" %(l[0])
	elif l[1] !=0:
		print "%s%.2fi" %("-" if l[1]<0 else "",abs(l[1]))
	else:
		print "0.00"

import math
a,b=[float(i) for i in raw_input().split()]
c,d=[float(i) for i in raw_input().split()]

mod1=a*a+b*b
mod2=c*c+d*d
add=[a+c,b+d]
sub=[a-c,b-d]

mul=[a*c-b*d,b*c+a*d]

div=[(a*c+b*d)/mod2,(b*c-a*d)/mod2]

print_c(add)
print_c(sub)
print_c(mul)
print_c(div)

print "%.2f\n%.2f" %(math.sqrt(mod1),math.sqrt(mod2))

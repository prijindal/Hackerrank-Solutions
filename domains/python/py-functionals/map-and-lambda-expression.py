n=int(raw_input())
list=[0,1]

for i in range(2,n):
	list.append(list[i-1]+list[i-2])

list =[i*i*i for i in list]

if n==0:
	list=[]
elif n==1:
	list=[0]

print list

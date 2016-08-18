def int_to_words(n):
	list=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen","twenty"];
	if n<=20:
		w=list[n]
	elif n>21 and n<30:
		w="twenty " + list[n-20]
	elif n==30:
		w="half"
	return w

def minutes(n):
	if n==0 or n==15 or n==45 or n==30:
		s="";
	elif n==1 or n==59:
		s="minute "
	else:
		s="minutes "
	return s

h=int(raw_input())
m=int(raw_input())

h_words=int_to_words(h)

if m==0:
	print(h_words+" o' clock");
elif m>30 :
	print(int_to_words(60-m)+" "+minutes(m)+"to "+int_to_words(h+1))
else :
	print(int_to_words(m)+" "+minutes(m)+"past "+h_words);

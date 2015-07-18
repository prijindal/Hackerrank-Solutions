#include<stdio.h>
int main()
{
	long t,n[1000],m[1000],c[1000],i,k,w,a;
	scanf("%ld",&t);
	for(i=0;i<t;++i)
	{
		scanf("%ld %ld %ld",&n[i],&c[i],&m[i]);
	}
	for(i=0;i<t;++i)
	{
		k=0;
		k+=n[i]/c[i];
		n[i]-=n[i]%c[i];
		w=k;
		while(w>=m[i])
		{
			a=w/m[i];
			k+=a;
			w=w%m[i];
			w+=a;
		}
		printf("%ld\n",k);
	}
}

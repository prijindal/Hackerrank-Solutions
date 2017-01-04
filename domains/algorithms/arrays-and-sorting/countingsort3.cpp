#include<iostream>
using namespace std;
int main()
{
	long i,n;
	cin>>n;
	long a[n];
	char s[100];
	for(i=0;i<n;++i)
	{
		cin>>a[i]>>s;
		//ans[i]=0;
	}
	for(i=1;i<=100;++i)
	{
		long k=0;
		for(long j=0;j<n;++j)
		{
			if(i>a[j])
			{
				k++;
			}
		}
		cout<<k<<" ";
	}
}

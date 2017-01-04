#include<iostream>
using namespace std;
int main()
{
	long i,n;
	cin>>n;
	long a[n];
	for(i=0;i<n;++i)
	{
		cin>>a[i];
	}
	for(i=0;i<100;++i)
	{
		long k=0;
		for(long j=0;j<n;++j)
		{
			if(i==a[j])
			{
				cout<<i<<" ";
			}
		}
		//cout<<k<<" ";
	}
}

#include<iostream>
using namespace std;
int main()
{
	int n,i,j,k,t;
	cin>>n;
	int a[n];
	for(i=0;i<n;++i)
	{
		cin>>a[i];
	}
	for(i=1;i<n;++i)
	{
		k=a[i];
		t=i;
		for(j=i;j>0;--j)
		{
			if(k<a[j-1])
			{
				a[j]=a[j-1];
				t=j-1;
			}
		}
		a[t]=k;
		for(j=0;j<n;++j)
		{
			cout<<a[j]<<" ";
		}
		cout<<endl;
	}
}

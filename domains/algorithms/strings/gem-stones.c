#include<stdio.h>
#include<string.h>
int main()
{
	int i,j,k,l,n,a,b,c;
	char str[100][100],m[100];
	fscanf(stdin,"%d",&n);
	for(i=0;i<n;i++)
	{
		fscanf(stdin,"%s",&str[i][0]);
	}

	c=0;
	i=0;
	for(j=0;j<strlen(str[i]);++j)
	{	b=0;
		for(k=0;k<n;++k)
		{
			a=0;
			for(l=0;l<strlen(str[k]);++l)
			{
				if(str[i][j]==str[k][l])
				{

					a=1;
				}
			}
			if(a==1)
			{
				b++;
			}
		}
		if(b>=n)
		{
			m[c]=str[i][j];
			c++;
		}
	}
	for(i=0;i<c;++i)
	{
		for(j=i+1;j<c;++j)
		{
			if(m[i]==m[j])
			{
				m[j]=0;
			}
		}
	}
	j=0;
	for(i=0;i<c;++i)
	{
		if(m[i]!=0)
		{
			j++;
		}
	}
	fprintf(stdout,"%d",j);
    return 0;
}

#include<stdio.h>
int main()
{
	int i,j,k,min;
	int width[100000],t,a[100000][2];
	int n;
	begin:
	//printf("Enter length of freeway and test cases");
	fscanf(stdin,"%d %d",&n,&t);
	/*if(((n<=2)||(n>100000))||((t<=1)||(t>=1000)))
	{
		printf("Wrong Input");
		goto begin;
	}
	if(n>1000)
	{
		min=1000;
	}
	else
	{
		min=n;
	}*/
	//printf("Enter Widths of Service lanes ");
	for(i=0;i<n;++i)
	{
		a:
		fscanf(stdin,"%d",&width[i]);
		/*if((width[k]>=3)||(width[k]<=1))
		{
			printf("Wrong input");
			goto a;
		}*/
	}
	//printf("Enter test cases\n");
	for(i=0;i<t;++i)
	{
		b:
		fscanf(stdin,"%d %d",&a[i][0],&a[i][1]);
		/*if(((a[i][0]<=0)||(a[i][0]>a[i][1]))||(a[i][1]>n))
		{
			printf("Wrong input");
			goto b;
		}*/
		/*j=a[i][1]-a[i][0]+1;
		if((j<=2)||(j>=min))
		{
			printf("Wrong Input");
			goto b;
		}*/
	}
	for(i=0;i<t;++i)
	{
		k=3;
		for(j=a[i][0];j<=a[i][1];j++)
		{
			if(width[j]==2)
			{
				k=2;
			}
		}
		for(j=a[i][0];j<=a[i][1];j++)
		{
			if(width[j]==1)
			{
				k=1;
			}
		}
		printf("%d\n",k);
	}
    return 0;
}

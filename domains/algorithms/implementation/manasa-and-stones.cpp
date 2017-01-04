#include<stdio.h>

int main() {
	int t;
	scanf("%i",&t);
	int input[t][3];

	for(int i=0;i<t;++i){
		scanf("%i %i %i",&input[i][0],&input[i][1],&input[i][2]);
	}

	for(int i=0;i<t;++i){
		int n=input[i][0];
		int a,b;
		int ans[n];
		if(input[i][1]<input[i][2]){
			a=input[i][1];
			b=input[i][2];
		}
		else{
			a=input[i][2];
			b=input[i][1];
		}
		for(int j=0;j<n;++j){
			ans[j]=(n-1-j)*a + j*b;
		}
		for(int j=0;j<n;++j){
			if(ans[j+1]!=ans[j]){
				printf("%i ",ans[j]);
			}
		}
		printf("\n");
	}

}

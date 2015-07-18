#include<stdio.h>

int main() {
	int t;
	scanf("%i",&t);
	int ans[t];

	for(int i=0;i<t;++i){
		int n,k;
		scanf("%i %i",&n,&k);

		int s=0;
		for(int j=0;j<n;++j){
			int a;
			scanf("%i",&a);
			if(a<=0){
				s++;
			}
		}
		if(s<k){
			ans[i]=1;
		}
		else{
			ans[i]=0;
		}
	}

	for(int i=0;i<t;++i){
		if(ans[i]){
			printf("YES");
		}
		else{
			printf("NO");
		}
		printf("\n");
	}

}

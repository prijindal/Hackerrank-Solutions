#include <iostream>
using namespace std;

// i,j <- current
// i,j-1
// i-1,j-1

int main() {
    int A[6][6];

    for(int i = 0;i<6;++i) {
        for(int j = 0;j<6;++j) {
            cin>>A[i][j];
        }
    }
    int max = -999999;
    for(int i = 1;i < 5;++i){
        for(int j = 1;j < 5;++j) {
            int sum = A[i][j];
            sum+=A[i-1][j];
            sum+=A[i+1][j];
            sum+=A[i-1][j-1];
            sum+=A[i+1][j-1];
            sum+=A[i-1][j+1];
            sum+=A[i+1][j+1];
            // cout<<"I: "<<i<<" j: "<<j<<" sum: "<<sum<<endl;
            if(sum > max) {
                max = sum;
            }
        }
    }

    cout<<max;
}

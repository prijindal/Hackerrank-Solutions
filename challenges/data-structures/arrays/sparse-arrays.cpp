#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin>>n;
    string A[n];
    for(int i = 0;i<n;++i) {
        cin>>A[i];
    }

    int q;
    cin>>q;
    for(int i = 0;i < q;++i) {
        string b;
        cin>>b;
        int k = 0;
        for(int j = 0;j< n;++j) {
            // cout<<"DEBUG, comapare: "<<b<<A[j]<<endl;
            if(b==A[j]) {
                k++;
            }
        }
        cout<<k<<endl;
    }
}

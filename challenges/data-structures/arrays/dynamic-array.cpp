#include <iostream>
#include <vector>

using namespace std;

int main() {
    int lastans = 0;
    int N,Q;
    cin>>N>>Q;
    vector<int> seq[N];
    for(int i =0;i < Q;++i) {
        int ch, x, y;
        cin>>ch>>x>>y;
        if(ch == 1) {
            seq[(x^lastans)%N].push_back(y);
        }
        else {
            vector<int> s = seq[(x^lastans)%N];
            lastans = s[y%s.size()];
            cout<<lastans<<endl;
        }
    }
}

#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n; 
        cin >> n;
        LL s=0;
        vector<LL> A(n);
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
            s += A[i];
        }
        LL sq = sqrtl(s);
        if( sq * sq == s){
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
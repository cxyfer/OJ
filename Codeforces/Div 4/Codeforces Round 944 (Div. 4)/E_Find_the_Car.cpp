#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5 + 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, k, q, x, idx;
    int A[N], B[N];
    cin >> t;
    while (t--) {
        cin >> n >> k >> q;
        for (int i = 1; i <= k; i++) cin >> A[i];
        for (int i = 1; i <= k; i++) cin >> B[i];
        vector<int> ans;
        while (q--) {
            cin >> x;
            idx = lower_bound(A, A+k, x) - A;
            if (A[idx] == x) ans.push_back(B[idx]);
            else ans.push_back(B[idx-1] + ((LL)(x - A[idx-1]) * (LL)(B[idx] - B[idx-1])) / (A[idx] - A[idx-1]));
            
        }
        for (int i = 0; i < ans.size(); i++) cout << ans[i] << " \n"[i == ans.size()-1];
        
    }
    return 0;
}
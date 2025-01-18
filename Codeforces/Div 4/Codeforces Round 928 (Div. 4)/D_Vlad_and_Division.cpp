#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<unsigned> A(n);
        for (int i = 0; i < n; ++i) cin >> A[i];
        map<int, bool> mp;
        int ans = n;
        for (int i = 0; i < n; ++i) {

            if (mp[A[i]]) {
                ans -= 1;
            }
            mp[~A[i]] = true;
        }
        cout << ans << "\n";
    }
    return 0;
}
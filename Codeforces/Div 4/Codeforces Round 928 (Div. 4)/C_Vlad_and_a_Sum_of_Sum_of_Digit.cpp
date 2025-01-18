#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 200005;


int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    
    int ans[N];
    ans[1] = 1;
    for (int i = 2; i < N; ++i) {
        int t = i, s = 0;
        while (t > 0) {
            s += t % 10;
            t /= 10;
        }
        ans[i] = ans[i - 1] + s;
    }

    while (t--) {
        int n;
        cin >> n;
        cout << ans[n] << '\n';
        // cout << n << '\n';
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n), cnt(n + 1);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int x : A) {
        if (x > n) continue; 
        cnt[x]++;
    }
    int ans = 0, s = 1;
    for (int i = 1; i <= n; i++) {
        if (cnt[i] == 0) break;
        ans = (ans + 1LL * s * cnt[i]) % MOD;
        s = (1LL * s * cnt[i]) % MOD;
    }
    cout << ans << endl;
    return 0;
}
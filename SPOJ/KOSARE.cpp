#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
#define endl '\n'

LL pow(LL a, LL b, LL MOD) {
    LL res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

void solve() {
    int n, B;
    cin >> n >> B;
    int U = 1 << B;
    vector<int> f(1 << B, 0);
    for (int i = 0; i < n; i++) {
        int m, x = 0, b;
        cin >> m;
        for (int j = 0; j < m; j++) {
            cin >> b;
            x |= (1 << (b - 1));
        }
        f[x]++;
    }

    for (int i = 0; i < B; i++) {
        int s = 0;
        while (s < U) {
            s |= (1 << i);
            f[s] += f[s ^ (1 << i)];
            s++;
        }
    }

    int ans = 0;
    for (int s = 0; s < U; s++) {
        int b = B - __builtin_popcount(s);
        if (b & 1) {
            ans -= pow(2, f[s], MOD) - 1;
            ans = (ans + MOD) % MOD;
        } else {
            ans = (ans + pow(2, f[s], MOD) - 1) % MOD;
        }
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}
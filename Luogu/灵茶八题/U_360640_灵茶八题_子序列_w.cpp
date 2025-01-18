#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
#define endl '\n'

LL qpow(LL a, LL b) {
    LL res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<LL> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    LL p = qpow(2, n - 1);
    LL ans = 0;
    for (int i = 0; i < n; i++) {
        ans += A[i] * p;
        ans %= MOD;
    }
    cout << ans << endl;
    return 0;
}
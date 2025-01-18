#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e8 + 7;
const int N = 6005;
#define endl '\n'

LL fact[N], inv[N];

LL qpow(LL a, LL b, LL p) {
    LL res = 1;
    while (b) {
        if (b & 1) res = res * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return res;
}

LL C(int n, int k) {
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;

    fact[0] = inv[0] = 1;
    for (int i = 1; i <= 2 * n; i++) {
        fact[i] = fact[i - 1] * i % MOD;
        inv[i] = qpow(fact[i], MOD - 2, MOD);
    }

    cout << C(2 * n, n) * qpow(n + 1, MOD - 2, MOD) % MOD << endl;
    return 0;
}
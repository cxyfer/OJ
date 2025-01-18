/*
    期望DP
    
    f[i] 表示從 i 到 n-1 的期望步數 (0-indexed)
    f[i] = 1 + sum_j=i^{i+A[i]}(f[j]) / (A[i] + 1)
    => (A[i] + 1) * f[i] = (A[i] + 1) + sum_j=i^{i+A[i]}(f[j])
    => A[i] * f[i] = (A[i] + 1) + sum_j={i+1}^{i+A[i]}(f[j])
    => f[i] = (A[i] + 1 + sum_j={i+1}^{i+A[i]}(f[j])) / A[i]
*/
#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
using LL = long long;
#define endl '\n'

LL qpow(LL a, LL b, LL mod) {
    LL res = 1;
    while (b) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<LL> A(n - 1);
    for (int i = 0; i < n - 1; i++) cin >> A[i];

    vector<LL> f(n);
    vector<LL> suf(n + 1);
    for (int i = n - 2; i >= 0; i--) {
        f[i] = (suf[i + 1] - suf[i + A[i] + 1] + A[i] + 1 + MOD) % MOD;
        f[i] = f[i] * qpow(A[i], MOD - 2, MOD) % MOD;
        suf[i] = (suf[i + 1] + f[i]) % MOD;
    }
    cout << f[0] << endl;

    return 0;
}
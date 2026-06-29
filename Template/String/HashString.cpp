#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

const long long MOD = 1'070'777'777;
const long long BASE = []() {
    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    return uniform_int_distribution<>(8e8, 9e8)(rng);
}();

class HashString {
public:
    int n;
    long long base, mod;
    vector<long long> P, H;

    HashString(const string& s, long long base, long long mod)
        : n((int)s.size()), base(base), mod(mod), P(n + 1), H(n + 1) {
        P[0] = 1;
        for (int i = 0; i < n; i++) {
            P[i + 1] = P[i] * base % mod;
            H[i + 1] = (H[i] * base + s[i]) % mod;
        }
    }

    long long query(int l, int r) const {
        return ((H[r + 1] - H[l] * P[r - l + 1] % mod) + mod) % mod;
    }
};
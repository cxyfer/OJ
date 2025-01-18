#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
#define endl '\n'

LL qpow(LL a, LL b, LL m) { // quick power
    LL ans = 1;
    while (b) {
        if (b & 1) ans = ans * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    cout << qpow(2, n, MOD) << endl;
    return 0;
}
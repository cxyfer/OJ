#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 100; // 不能求反元素
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<LL> f(n + 1);
    f[0] = f[1] = 1;
    for (int i = 2; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            f[i] = (f[i] + f[j] * f[i - j - 1]) % MOD;
        }
    }
    cout << f[n] << endl;
    return 0;
}
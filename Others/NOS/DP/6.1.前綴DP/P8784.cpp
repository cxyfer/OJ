/*
P8784 [蓝桥杯 2022 省 B] 积木画
https://www.luogu.com.cn/problem/P8784
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<vector<LL>> f(2, vector<LL>(4));
    f[1 & 1][0] = f[1 & 1][3] = 1;
    for (int i = 2; i <= n; i++) {
        f[i & 1][0] = f[(i - 1) & 1][3];
        f[i & 1][1] = (f[(i - 1) & 1][0] + f[(i - 1) & 1][2]) % MOD;
        f[i & 1][2] = (f[(i - 1) & 1][0] + f[(i - 1) & 1][1]) % MOD;
        f[i & 1][3] = (f[(i - 1) & 1][0] + f[(i - 1) & 1][1] + f[(i - 1) & 1][2] + f[(i - 1) & 1][3]) % MOD;
    }
    cout << f[n & 1][3] << endl;
    return 0;
}
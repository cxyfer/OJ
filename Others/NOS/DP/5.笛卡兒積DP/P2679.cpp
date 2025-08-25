/*
 * P2679 [NOIP 2015 提高组] 子串
 * https://www.luogu.com.cn/problem/P2679
 */
#include <bits/stdc++.h>
using namespace std;
using u32 = uint32_t;
const u32 MOD = 1e9 + 7;
#define endl '\n'

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    string A, B;
    cin >> A >> B;

    u32 f[2][m + 1][k + 1][2];
    memset(f, 0, sizeof(f));
    f[0][0][0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        int cur = i & 1, pre = (i - 1) & 1;
        f[cur][0][0][0] = 1;
        for (int j = 1; j <= m; ++j) {
            for (int t = 1; t <= k; ++t) {
                f[cur][j][t][0] = (f[pre][j][t][0] + f[pre][j][t][1]) % MOD;
                if (A[i - 1] == B[j - 1]) {
                    f[cur][j][t][1] =
                        (f[pre][j - 1][t][1] + f[pre][j - 1][t - 1][0] +
                         f[pre][j - 1][t - 1][1]) %
                        MOD;
                } else {
                    f[cur][j][t][1] = 0;
                }
            }
        }
    }
    cout << (f[n & 1][m][k][0] + f[n & 1][m][k][1]) % MOD << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve();
    return 0;
}
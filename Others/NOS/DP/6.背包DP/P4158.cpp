/*
P4158 [SCOI2009] 粉刷匠
https://www.luogu.com.cn/problem/P4158
狀態機DP + 分組背包DP
*/
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#define endl '\n'

void solve() {
    int N, M, T;
    cin >> N >> M >> T;
    // f[t] 表示粉刷 t 次時，能獲得的最大價值
    vector<int> f(T + 1);
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        // g[i][j][0/1/2] 表示考慮到字串的前 i 個字元，粉刷 j 次，最後一個粉刷成紅色/藍色/未粉刷時，能獲得的最大價值
        vector<vector<array<int, 3>>> g(2, vector<array<int, 3>>(T + 1));
        for (int i = 1; i <= M; i++) {
            auto ch = s[i - 1];
            auto &curr = g[i & 1], &prev = g[(i - 1) & 1];
            for (int j = 1; j <= T; j++) {
                curr[j][0] = max({prev[j][0], prev[j - 1][1], prev[j - 1][2]}) + (ch == '0');
                curr[j][1] = max({prev[j - 1][0], prev[j][1], prev[j - 1][2]}) + (ch == '1');
                curr[j][2] = ranges::max(prev[j]);
            }
        }
        // 分組背包
        vector<pair<int, int>> items;
        for (int t = 1; t <= T; t++)
            items.emplace_back(t, ranges::max(g[M & 1][t]));
        for (int j = T; j >= 0; j--)
            for (auto [t, c] : items)
                if (j >= t)
                    f[j] = max(f[j], f[j - t] + c);
    }
    cout << ranges::max(f) << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}
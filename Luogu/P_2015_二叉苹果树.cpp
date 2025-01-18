#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, u, v, w;
    cin >> n >> q;
    vector<vector<pair<int, int>>> g(n);
    for (int i = 1; i < n; i++) {
        cin >> u >> v >> w;
        g[u - 1].emplace_back(v - 1, w);
        g[v - 1].emplace_back(u - 1, w);
    }
    vector<vector<int>> dp(n, vector<int>(q + 1, 0));
    auto dfs = [&](auto &&dfs, int u, int fa) -> int {
        vector<pair<int, int>> child;
        for (auto [v, w] : g[u]) {
            if (v == fa) continue;
            child.emplace_back(v, w);
        }
        if (child.size() == 0) return 0;
        int ls = child[0].first, lv = child[0].second;
        int rs = child[1].first, rv = child[1].second;
        int sz = dfs(dfs, ls, u) + dfs(dfs, rs, u) + 2;
        for (int k = 0; k <= min(sz, q); k++) {
            for (int i = 0; i <= k; i++) {
                int j = k - i;
                int left = i > 0 ? dp[ls][i - 1] + lv : 0;
                int right = j > 0 ? dp[rs][j - 1] + rv : 0;
                dp[u][k] = max(dp[u][k], left + right);
            }
        }
        return sz;
    };
    dfs(dfs, 0, -1);
    cout << dp[0][q] << endl;
    return 0;
}
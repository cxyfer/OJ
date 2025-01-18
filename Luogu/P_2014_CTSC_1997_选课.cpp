#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, w;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> W(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> u >> w;
        g[u].push_back(i);
        W[i] = w;
    }
    // f[u][k] 表示以 u 為根的子樹中選 k 門課的最大價值
    vector<vector<int>> f(n + 1, vector<int>(m + 1));
    auto dfs = [&](auto &&dfs, int u) -> int {
        int sz = 1;
        for (int v : g[u]) {
            int v_sz = dfs(dfs, v);
            sz += v_sz;
            // 分組背包
            // 枚舉 u 子樹選課數量，為了避免覆蓋尚未計算的狀態，從大到小枚舉
            for (int k = min(sz, m); k >= 1; k--)
                // 枚舉 v 子樹選課數量
                for (int i = 1; i <= min(k, v_sz); i++)
                    f[u][k] = max(f[u][k], f[u][k - i] + f[v][i]);
        }
        if (u != 0) {
            // 如果 u 不是根節點，則需要選 u 這門課
            for (int k = m; k >= 1; k--) f[u][k] = f[u][k - 1] + W[u];
        }
        return sz;
    };
    dfs(dfs, 0);
    cout << f[0][m] << endl;
    return 0;
}
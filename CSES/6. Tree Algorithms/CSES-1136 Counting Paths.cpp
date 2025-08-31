#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class LCA {
    int n, m;
    vector<int> dep;
    vector<vector<int>> pa;  // pa[u][i] 表示 u 的第 2^i 個祖先
public:
    LCA(vector<vector<int>>& g) {
        n = g.size();
        m = bit_width(static_cast<unsigned>(n));
        dep.resize(n);
        pa.resize(n, vector<int>(m, -1));

        // DFS 處理 dep[u] 和 pa[u][0]
        auto dfs = [&](auto&& dfs, int u, int fa) -> void {
            pa[u][0] = fa;
            for (auto& v : g[u]) {
                if (v == fa) continue;
                dep[v] = dep[u] + 1;
                dfs(dfs, v, u);
            }
        };
        dfs(dfs, 0, -1);

        // 倍增處理 pa[u][i]
        for (int i = 0; i < m - 1; i++)
            for (int u = 0; u < n; u++)
                if (pa[u][i] != -1) pa[u][i + 1] = pa[pa[u][i]][i];
    }

    // 返回 u 的第 k 個祖先，可以用 lowbit 加速
    int get_kth_ancestor(int u, int k) {
        for (; k && u != -1; k &= k - 1)  // 當 u 被更新成 -1 後就不能再往上跳了，提前退出
            u = pa[u][bit_width(static_cast<unsigned>(k & -k)) - 1];
        return u;
    }

    // 返回 u 和 v 的 LCA
    int get_lca(int u, int v) {
        if (dep[u] > dep[v]) swap(u, v);
        v = get_kth_ancestor(v, dep[v] - dep[u]);  // 使 u 和 v 在同一深度
        if (v == u) return u;
        for (int i = m - 1; i >= 0; i--) {
            int fu = pa[u][i], fv = pa[v][i];
            // 同時往上跳 2^i 步後還不會相遇
            if (fu != fv) u = fu, v = fv;
        }
        return pa[u][0];  // 再往上跳一步就是答案
    }

    // 返回 u 到 v 的距離，如果是有權圖則需要改成使用 dist 計算
    long long get_dis(int u, int v) {
        return dep[u] + dep[v] - dep[get_lca(u, v)] * 2;
    }
};

void solve() {
    int n, q, u, v, z;
    cin >> n >> q;
    vector<vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
        cin >> u >> v;
        g[u - 1].push_back(v - 1);
        g[v - 1].push_back(u - 1);
    }

    LCA lca(g);
    vector<int> f(n);  // 差分
    for (int i = 0; i < q; i++) {
        cin >> u >> v;
        f[u - 1]++;
        f[v - 1]++;
        z = lca.get_lca(u - 1, v - 1);
        f[z]--;
        if (z != 0) f[lca.get_kth_ancestor(z, 1)]--;
    }

    auto dfs = [&](auto&& dfs, int u, int fa) -> void {
        for (auto& v : g[u]) {
            if (v == fa) continue;
            dfs(dfs, v, u);
            f[u] += f[v];
        }
    };
    dfs(dfs, 0, -1);
    for (int i = 0; i < n; i++) cout << f[i] << " \n"[i == n - 1];
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}
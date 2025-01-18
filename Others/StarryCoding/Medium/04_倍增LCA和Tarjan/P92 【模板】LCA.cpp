#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class TreeAncestor {
    vector<int> dep;
    vector<vector<int>> pa;
public:
    TreeAncestor(vector<pair<int, int>> &edges, int root = 0) {
        int n = edges.size() + 1;
        int m = 32 - __builtin_clz(n); // n.bit_length()
        vector<vector<int>> g(n); // 0-indexed
        for (auto [x, y]: edges) {
            g[x].push_back(y);
            g[y].push_back(x);
        }

        dep.resize(n);
        pa.resize(n, vector<int>(m, -1));
        function<void(int, int)> dfs = [&](int u, int fa) {
            pa[u][0] = fa;
            for (int v: g[u]) {
                if (v != fa) {
                    dep[v] = dep[u] + 1;
                    dfs(v, u);
                }
            }
        };
        dfs(root, -1);

        for (int i = 0; i < m - 1; i++)
            for (int u = 0; u < n; u++) {
                int p = pa[u][i];
                if (p != -1)
                    pa[u][i + 1] = pa[p][i];
            }
    }

    int get_kth_ancestor(int node, int k) {
        for (; k; k &= k - 1)
            node = pa[node][__builtin_ctz(k)];
        return node;
    }

    // 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    int get_lca(int x, int y) {
        if (depth[x] > depth[y])
            swap(x, y);
        // 使 y 和 x 在同一深度
        y = get_kth_ancestor(y, depth[y] - depth[x]);
        if (y == x)
            return x;
        for (int i = pa[x].size() - 1; i >= 0; i--) {
            int px = pa[x][i], py = pa[y][i];
            if (px != py) {
                x = px;
                y = py;
            }
        }
        return pa[x][0];
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<fa
    return 0;
}
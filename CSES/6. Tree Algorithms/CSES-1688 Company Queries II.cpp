#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n, q, fa;
    cin >> n >> q;
    int m = bit_width(static_cast<unsigned>(n));

    vector<int> dep(n);
    vector<vector<int>> pa(n, vector<int>(m, -1));
    for (int u = 1; u < n; u++) {
        cin >> fa;
        fa -= 1;
        pa[u][0] = fa;
        dep[u] = dep[fa] + 1;
    }

    // 用倍增法更新 pa
    for (int i = 0; i < m - 1; i++)
        for (int u = 0; u < n; u++)
            if (pa[u][i] != -1) pa[u][i + 1] = pa[pa[u][i]][i];

    auto get_kth_ancestor = [&](int u, int k) -> int {
        for (; k && u != -1; k &= k - 1)
            u = pa[u][bit_width(static_cast<unsigned>(k & -k)) - 1];
        return u;
    };

    auto get_lca = [&](int u, int v) -> int {
        if (dep[u] > dep[v]) swap(u, v);
        v = get_kth_ancestor(v, dep[v] - dep[u]);  // 使 u 和 v 在同一深度
        if (v == u) return u;
        for (int i = m - 1; i >= 0; i--) {
            int fu = pa[u][i], fv = pa[v][i];
            // 同時往上跳 2^i 步後還不會相遇
            if (fu != fv) u = fu, v = fv;
        }
        return pa[u][0];  // 再往上跳一步就是答案
    };

    while (q--) {
        int u, v;
        cin >> u >> v;
        u -= 1, v -= 1;
        cout << get_lca(u, v) + 1 << endl;
    }
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
#ifdef LOCAL
    ifstream fin("input.txt");
    cin.rdbuf(fin.rdbuf());
#endif
    solve();
    return 0;
}
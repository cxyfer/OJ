#include <bits/stdc++.h>
using LL = long long;
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, u, v;
    cin >> n;
    vector<vector<int>> g(n);
    for (int i = 1; i < n; i++) {
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<LL> sz(n), dep(n), f(n);
    auto dfs1 = [&](auto dfs1, int u, int fa) -> int {
        sz[u] = 1;
        f[0] += dep[u];
        for (int v : g[u]) {
            if (v == fa) continue;
            dep[v] = dep[u] + 1;
            sz[u] += dfs1(dfs1, v, u);
        }
        return sz[u];
    };
    dfs1(dfs1, 0, -1);

    LL ans = 1;
    auto dfs2 = [&](auto dfs2, int u, int fa) -> void {
        if (f[u] > f[ans]) ans = u;
        for (int v : g[u]) {
            if (v == fa) continue;
            f[v] = f[u] - sz[v] + (n - sz[v]);
            dfs2(dfs2, v, u);
        }
    };
    dfs2(dfs2, 0, -1);
    cout << ans + 1 << endl;
    return 0;
}
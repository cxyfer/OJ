#include <bits/stdc++.h>
using LL = long long;
using namespace std;
const LL INF = 1e18;
#define endl '\n'
#define PII pair<int, int>

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n, u, v, w, tot = 0;
    cin >> n;
    vector<int> c(n);
    vector<vector<PII>> g(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
        tot += c[i];
    }
    for (int i = 1; i < n; i++) {
        cin >> u >> v >> w;
        u--, v--;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }

    vector<LL> sz(n), dep(n), f(n);
    auto dfs1 = [&](auto dfs1, int u, int fa) -> void {
        sz[u] = c[u];
        for (auto [v, w] : g[u]) {
            if (v == fa) continue;
            dep[v] = dep[u] + 1;
            dfs1(dfs1, v, u);
            sz[u] += sz[v];
            f[u] += f[v] + w * sz[v];
        }
    };
    dfs1(dfs1, 0, -1);

    LL ans = INF;
    auto dfs2 = [&](auto dfs2, int u, int fa) -> void {
        ans = min(ans, f[u]);
        for (auto [v, w] : g[u]) {
            if (v == fa) continue;
            f[v] = f[u] - sz[v] * w + (tot - sz[v]) * w;
            dfs2(dfs2, v, u);
        }
    };
    dfs2(dfs2, 0, -1);
    cout << ans << endl;
    return 0;
}
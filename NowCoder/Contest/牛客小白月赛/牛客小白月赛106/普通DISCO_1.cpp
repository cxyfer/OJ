#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, u, v;
    cin >> n;
    vector<vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
        cin >> u >> v;
        u--; v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<int> fa(n, -1);
    vector<int> dep(n, 1);
    auto dfs = [&](auto dfs, int u) -> void {
        for (int v : g[u]) {
            if (v == fa[u]) continue;
            fa[v] = u;
            dep[v] = dep[u] + 1;
            dfs(dfs, v);
        }
    };
    dfs(dfs, 0);

    int idx = 0;
    for (int u = 0; u < n; u++) {
        if (dep[u] > dep[idx]) idx = u;
    }

    queue<pair<int, int>> q;
    vector<bool> vis(n, false);
    int t = idx;
    while (t != -1) {
        q.push({0, t});
        vis[t] = true;
        t = fa[t];
    }

    int ans = 1;
    while (!q.empty()) {
        auto [d, u] = q.front(); q.pop();
        ans = max(ans, d);
        for (int v : g[u]) {
            if (vis[v]) continue;
            vis[v] = true;
            q.push({d + 1, v});
        }
    }
    cout << ans + dep[idx] - 1 << endl;
    return 0;
}
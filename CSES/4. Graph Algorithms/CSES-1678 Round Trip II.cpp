#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    vector<vector<int>> g(n);
    for (int i = 0; i < m; ++i) {
        cin >> u >> v;
        g[u - 1].push_back(v - 1);
    }

    vector<int> fa(n, -1), vis(n, 0);
    auto dfs = [&](auto &&dfs, int u) -> void {
        vis[u] = 1;
        for (int v : g[u]) {
            if (vis[v] == 1) {
                vector<int> ans = {u};
                int t = u;
                while (t != v) {
                    ans.push_back(fa[t]);
                    t = fa[t];
                }
                ans.push_back(u);
                reverse(ans.begin(), ans.end());
                cout << ans.size() << endl;
                for (int x : ans) cout << x + 1 << " ";
                cout << endl;
                exit(0);
            }
            if (vis[v] == 2) continue;
            fa[v] = u;
            dfs(dfs, v);
        }
        vis[u] = 2;
        return;
    };

    for (int u = 0; u < n; ++u) {
        if (vis[u]) continue;
        dfs(dfs, u);
    }
    cout << "IMPOSSIBLE" << endl;
    return 0;
}
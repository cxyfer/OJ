#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    vector<vector<int>> g(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        u--; v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    vector<int> fa(n);
    vector<bool> vis(n);
    auto dfs = [&](auto &&dfs, int u) -> void {
        for (int v : g[u]) {
            if (v == fa[u]) continue;
            if (vis[v]) {
                vector<int> path = {u};
                while (path.back() != v) {
                    path.push_back(fa[path.back()]);
                }
                path.push_back(u);
                cout << path.size() << endl;
                for (int i = 0; i < path.size(); i++) {
                    cout << path[i] + 1 << " \n"[i == path.size() - 1];
                }
                exit(0);
            }
            vis[v] = true;
            fa[v] = u;
            dfs(dfs, v);
        }
        return;
    };
    for (int i = 0; i < n; i++) {
        if (vis[i]) continue;
        vis[i] = true;
        dfs(dfs, i);
    }
    cout << "IMPOSSIBLE" << endl;
    return 0;
}
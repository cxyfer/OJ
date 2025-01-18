#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define PII pair<int, int>

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    vector<vector<PII>> g(n);
    vector<int> deg(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        u--; v--;
        g[u].push_back({v, i});
        g[v].push_back({u, i});
        deg[u]++;
        deg[v]++;
    }

    for (int i = 0; i < n; i++) {
        if (deg[i] & 1) {
            cout << "IMPOSSIBLE" << endl;
            return 0;
        }
    }

    vector<bool> used(m);
    vector<int> path;
    auto dfs = [&](auto &dfs, int u) -> void {
        while (!g[u].empty()) {
            auto [v, eid] = g[u].back();
            g[u].pop_back();
            if (used[eid]) continue;
            used[eid] = true;
            dfs(dfs, v);
        }
        path.push_back(u + 1);
    };
    dfs(dfs, 0);

    if (path.size() != m + 1) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        reverse(path.begin(), path.end());
        for (int i = 0; i < m + 1; i++) {
            cout << path[i] << " \n"[i == m];
        }
    }
    return 0;
}
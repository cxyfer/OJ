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
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<int> colors(n, 0);
    auto dfs = [&](auto dfs, int u) -> bool {
        int c = colors[u];
        for (int v : g[u]) {
            if (colors[v] == c) return false;
            if (colors[v]) continue;
            colors[v] = 3 - c;
            if (!dfs(dfs, v)) return false;
        }
        return true;
    };

    for (int i = 0; i < n; i++) {
        if (colors[i]) continue;
        colors[i] = 1;
        if (!dfs(dfs, i)) {
            cout << "IMPOSSIBLE" << endl;
            return 0;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << colors[i] << " \n"[i == n - 1];
    }
    return 0;
}
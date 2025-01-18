#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        g[u].push_back(v);
    }

    vector<bool> vis(n + 1);
    queue<int> q;
    q.push(1);
    vis[1] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : g[u]) if (!vis[v]) q.push(v), vis[v] = true;
    }

    for (int u = 1; u <= n; u++) if (vis[u]) cout << u << ' ';
    cout << endl;
    return 0;
}
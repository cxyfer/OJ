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

    vector<int> pre(n, -1);
    vector<bool> vis(n, false);
    queue<int> q;
    q.push(0);
    vis[0] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : g[u]) {
            if (vis[v]) continue;
            vis[v] = true;
            pre[v] = u;
            q.push(v);
        }
    }
    if (pre[n - 1] == -1) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        vector<int> ans;
        for (int u = n - 1; u != -1; u = pre[u]) ans.push_back(u);
        reverse(ans.begin(), ans.end());
        cout << ans.size() << endl;
        for (int u : ans) cout << u + 1 << " ";
        cout << endl;
    }
    return 0;
}
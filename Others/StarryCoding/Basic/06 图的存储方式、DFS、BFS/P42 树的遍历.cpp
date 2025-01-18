#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n;
    vector<vector<int>> g(n + 1);
    for (int i = 2; i <= n ; i++) cin >> x, g[x].push_back(i);

    vector<int> dfn, bfn;

    auto dfs = [&](auto &&dfs, int u, int fa) -> void {
        dfn.push_back(u);
        for (int v : g[u]) if (v != fa) dfs(dfs, v, u);
    };
    dfs(dfs, 1, 0);

    queue<int> q;
    vector<bool> vis(n + 1);
    q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        bfn.push_back(u);
        for (int v : g[u]) if (!vis[v]) q.push(v), vis[v] = true;
    }

    for (int i = 0; i < n; i++) cout << dfn[i] << " \n"[i == n - 1];
    for (int i = 0; i < n; i++) cout << bfn[i] << " \n"[i == n - 1];
    return 0;
}
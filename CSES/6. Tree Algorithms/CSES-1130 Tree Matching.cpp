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
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<bool> used(n);
    int ans = 0;
    auto dfs = [&](auto dfs, int u, int fa) -> void {
        for (int v : g[u]) {
            if (v == fa) continue;
            dfs(dfs, v, u);
            if (!used[u] && !used[v]) {
                used[u] = used[v] = true;
                ans++;
            }
        }
    };
    dfs(dfs, 0, -1);
    cout << ans << endl;
    return 0;
}
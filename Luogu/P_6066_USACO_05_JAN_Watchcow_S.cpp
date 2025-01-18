#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    // Hierholzer's Algorithm 
    vector<int> path;
    auto dfs = [&](auto &&dfs, int u) -> void {
        while (!g[u].empty()) {
            int v = g[u].back();
            g[u].pop_back();
            dfs(dfs, v);
        }
        path.push_back(u);
    };
    dfs(dfs, 1);

    // 輸出答案
    reverse(path.begin(), path.end());
    for (int i = 0; i < path.size(); ++i) {
        cout << path[i] << endl;
    }
    return 0;
}
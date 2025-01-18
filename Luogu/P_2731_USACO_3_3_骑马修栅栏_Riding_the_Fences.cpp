#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int m, u, v;
    cin >> m;
    unordered_map<int, vector<int>> g;
    unordered_map<int, int> deg;
    for (int i = 0; i < m; ++i) {
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    int st = INT_MAX, mn = INT_MAX;
    for (auto &[u, val] : deg) {
        mn = min(mn, u);
        sort(g[u].begin(), g[u].end(), greater<int>());
        if (val & 1) {
            st = min(st, u);
        }
    }
    if (st == INT_MAX) st = mn;
    vector<int> ans;
    auto dfs = [&](auto &&dfs, int u) -> void {
        while (!g[u].empty()) {
            int v = g[u].back(); g[u].pop_back();
            g[v].erase(find(g[v].begin(), g[v].end(), u));
            dfs(dfs, v);
        }
        ans.push_back(u);
    };
    dfs(dfs, st);
    for (auto it = ans.rbegin(); it != ans.rend(); ++it) {
        cout << *it << endl;
    }
    return 0;
}
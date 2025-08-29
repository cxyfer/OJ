#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 998244353;
#define endl '\n'

void solve() {
    int n, m, V;
    cin >> n >> m >> V;
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    vector<vector<int>> g(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    
    // 1. Find bridges (cut edges) by Tarjan's algorithm
    int time = 0;
    vector<int> dfn(n, -1), low(n, -1);
    set<pair<int, int>> bridges;
    auto dfs = [&](this auto&& dfs, int u, int fa) -> void {
        dfn[u] = low[u] = time++;
        for (int v : g[u]) {
            if (v == fa) continue;
            if (dfn[v] != -1) // back edge
                low[u] = min(low[u], dfn[v]);
            else {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > dfn[u]) bridges.insert({min(u, v), max(u, v)});
            }
        }
    };
    dfs(0, -1);

    // 2. Find BCCs (biconnected components) by DFS
    vector<int> comp(n, -1);
    int idx = 0;
    auto dfs2 = [&](this auto&& dfs2, int u) -> void {
        comp[u] = idx;
        for (int v : g[u]) {
            if (comp[v] != -1 || bridges.find({min(u, v), max(u, v)}) != bridges.end()) continue;
            dfs2(v);
        }
    };
    for (int u = 0; u < n; u++) {
        if (comp[u] != -1) continue;
        dfs2(u);
        idx++;
    }
    
    vector<vector<int>> bccs(idx);
    for (int i = 0; i < n; i++) bccs[comp[i]].push_back(i);
    
    // 3. Process each BCC
    LL ans = 1;

    vector<int> color(n, -1);
    auto bipartite = [&](this auto&& bipartite, int u) -> bool {
        queue<pair<int, int>> q;
        q.push({u, 0});
        color[u] = 0;
        while (!q.empty()) {
            auto [u, c] = q.front(); q.pop();
            for (int v : g[u]) {
                if (bridges.find({min(u, v), max(u, v)}) != bridges.end()) continue;
                if (color[v] == -1) {
                    color[v] = c ^ 1;
                    q.push({v, c ^ 1});
                }
                else if (color[v] == c) return false;
            }
        }
        return true;
    };

    for (auto bcc : bccs) {
        // a. Check consistency of weights and determine common weight
        int weight = -1;
        for (int u : bcc) {
            if (A[u] == -1) continue;
            if (weight != -1 && A[u] != weight) {
                cout << 0 << endl;
                return;
            }
            weight = A[u];
        }

        // b. Check for odd cycles (bipartite coloring)
        bool is_bipartite = bipartite(bcc[0]);

        // c. Calculate the number of ways
        if (!is_bipartite) {
            if (weight != -1 && weight != 0) {
                cout << 0 << endl;
                return;
            }
        }
        else if (weight == -1) ans = (ans * V) % MOD;
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
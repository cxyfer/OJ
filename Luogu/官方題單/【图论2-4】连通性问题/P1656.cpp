#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

template <typename T>
class Tarjan {
public:
    /* 建圖*/
    int n;
    vector<vector<T>> g;

    /* Tarjan & BCC & v-BCC 相關 */
    vector<T> dfn, low;
    int time;
    set<pair<T, T>> bridges;

    Tarjan(int n) : n(n) {
        g.resize(n);
        dfn.assign(n, -1);
        low.assign(n, -1);
    }

    void add_edge(int u, int v) {
        g[u].push_back(v);
        g[v].push_back(u);
    }

    void dfs1(int u, int fa) {
        dfn[u] = low[u] = time++;
        for (auto v : g[u]) {
            if (v == fa) continue;
            if (dfn[v] != -1)
                low[u] = min(low[u], dfn[v]);
            else {
                dfs1(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > dfn[u])  // bridge
                    bridges.insert({min(u, v), max(u, v)});
            }
        }
    }

    void run() {
        for (int u = 0; u < n; u++)
            if (dfn[u] == -1) dfs1(u, -1);
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    Tarjan<int> T(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        T.add_edge(u - 1, v - 1);
    }
    T.run();
    for (auto [u, v] : T.bridges)
        cout << u + 1 << " " << v + 1 << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
#ifdef LOCAL
    ifstream fin("input.txt");
    cin.rdbuf(fin.rdbuf());
#endif
    int t = 1;
    while (t--) solve();
    return 0;
}
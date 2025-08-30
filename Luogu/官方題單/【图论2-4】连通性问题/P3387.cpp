#include <bits/stdc++.h>

#include <ranges>

using namespace std;
#define endl '\n'

class SCC {
public:
    /* 建圖*/
    int n;
    vector<vector<int>> g;

    /* Tarjan & SCC 相關 */
    int time;
    vector<int> dfn, low, stk;
    vector<bool> in_stk;
    vector<int> scc_id;
    vector<vector<int>> sccs;

    SCC(int n) : n(n) {
        g.resize(n);
        time = 0;
        dfn.assign(n, -1);
        low.assign(n, -1);
        in_stk.assign(n, false);
        scc_id.assign(n, -1);
        sccs.clear();
    }

    void add_edge(int u, int v) {
        g[u].push_back(v);
    }

    void dfs(int u) {
        dfn[u] = low[u] = time++;
        stk.push_back(u);
        in_stk[u] = true;
        for (auto v : g[u]) {
            if (dfn[v] == -1) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (in_stk[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
        if (dfn[u] == low[u]) {
            int v;
            vector<int> scc;
            while (true) {
                v = stk.back();
                stk.pop_back();
                in_stk[v] = false;
                scc_id[v] = sccs.size();
                scc.push_back(v);
                if (v == u) break;
            }
            sccs.push_back(scc);
        }
    }

    void run() {
        for (int u = 0; u < n; u++)
            if (dfn[u] == -1) dfs(u);
    }
};

void solve() {
    int n, m, u, v;
    cin >> n >> m;
    SCC T(n);
    vector<int> A(n);
    for (auto& x : A) cin >> x;
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        T.add_edge(u - 1, v - 1);
    }

    T.run();

    int k = T.sccs.size();
    vector<int> f(k, 0);
    for (auto [i, scc] : views::enumerate(T.sccs)) {
        int val = 0;
        for (auto u : scc) {
            val += A[u];
            for (auto v : T.g[u]) f[i] = max(f[i], f[T.scc_id[v]]);
        }
        f[i] += val;
    }
    cout << ranges::max(f) << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifdef LOCAL
    ifstream fin("input.txt");
    cin.rdbuf(fin.rdbuf());
#endif
    solve();
    return 0;
}
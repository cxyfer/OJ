#include <bits/stdc++.h>
using namespace std;
using LL = long long;
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
            }
            else if (in_stk[v]) {
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
    int n, m, i, x, j, y;
    cin >> n >> m;
    SCC T(2 * n);
    for (int _ = 0; _ < m; _++) {
        cin >> i >> x >> j >> y;
        i--, j--;
        T.add_edge(i + n * (1 - x), j + n * y);
        T.add_edge(j + n * (1 - y), i + n * x);
    }

    T.run();

    for (int i = 0; i < n; i++) {
        if (T.scc_id[i] == T.scc_id[i + n]) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }

    vector<int> ans(n, -1);
    for (int i = 0; i < n; i++)
        ans[i] = T.scc_id[i] < T.scc_id[i + n] ? 0 : 1;
    cout << "POSSIBLE" << endl;
    for (int i = 0; i < n; i++) cout << ans[i] << " \n"[i == n - 1];
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
#ifdef LOCAL
    ifstream fin("input.txt");
    cin.rdbuf(fin.rdbuf());
#endif
    solve();
    return 0;
}
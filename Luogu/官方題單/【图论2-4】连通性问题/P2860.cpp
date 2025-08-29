#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

template<typename T>
class Tarjan {
public:
    /* 建圖*/
    int n;
    vector<vector<T>> g;

    /* Tarjan & BCC & v-BCC 相關 */
    vector<T> dfn, low;
    vector<T> stk;
    int time;
    set<pair<T, T>> bridges;
    vector<int> bcc_id;
    vector<vector<T>> bccs;

    Tarjan(int n) : n(n) {
        g.resize(n);
        dfn.assign(n, -1);
        low.assign(n, -1);
        bcc_id.assign(n, -1);
    }

    void add_edge(int u, int v) {
        g[u].push_back(v);
        g[v].push_back(u);
    }

    void dfs1(int u, int fa) {
        dfn[u] = low[u] = time++;
        stk.push_back(u);
        int cnt = 0;
        for (auto v : g[u]) {
            if (v == fa) continue;
            if (dfn[v] != -1)
                low[u] = min(low[u], dfn[v]);
            else {
                cnt++;
                dfs1(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > dfn[u])  // bridge
                    bridges.insert({min(u, v), max(u, v)});
            }
        }
    }

    void dfs2(int u) {
        bcc_id[u] = bccs.size() - 1;
        bccs.back().push_back(u);
        for (auto v : g[u]) {
            if (bcc_id[v] != -1 || bridges.count({min(u, v), max(u, v)}))
                continue;
            dfs2(v);
        }
    }

    void run() {
        for (int u = 0; u < n; u++)
            if (dfn[u] == -1) dfs1(u, -1), stk.clear();
        for (int u = 0; u < n; u++)
            if (bcc_id[u] == -1) bccs.push_back(vector<T>()), dfs2(u);
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

    vector<int> deg(T.bccs.size(), 0);
    for (auto [u, v] : T.bridges) {
        deg[T.bcc_id[u]]++;
        deg[T.bcc_id[v]]++;
    }
    int k = count(deg.begin(), deg.end(), 1);
    cout << (k + 1) / 2 << endl;
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
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
    vector<bool> vis;
    vector<T> stk;
    int time;
    set<pair<T, T>> bridges;
    vector<int> bcc_id;
    vector<vector<T>> bccs;
    vector<bool> cut_vertices;

    /* 圓方樹 (Block-Cut Tree) 相關 */
    int bct_sz;
    vector<vector<T>> bct;
    vector<T> weights;

    Tarjan(int n) : n(n) {
        g.resize(n);
        dfn.assign(n, -1);
        low.assign(n, -1);
        vis.assign(n, false);
        bcc_id.assign(n, -1);
        cut_vertices.assign(n, false);
        bct.resize(2 * n);
        weights.assign(2 * n, 0);
        for (int i = 0; i < n; i++) weights[i] = -1;
        bct_sz = n;
    }

    void add_edge(int u, int v) {
        g[u].push_back(v);
        g[v].push_back(u);
    }

    void add_bct_edge(int u, int v) {
        bct[u].push_back(v);
        bct[v].push_back(u);
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
                if (low[v] >= dfn[u]) {  // v-BCC & Block-Cut Tree
                    int s = bct_sz++;
                    weights[s] = 1;
                    add_bct_edge(s, u);
                    int w;
                    do {
                        w = stk.back();
                        stk.pop_back();
                        add_bct_edge(s, w);
                        weights[s]++;
                    } while (w != v);
                }
            }
        }
    }

    void run() {
        for (int u = 0; u < n; u++)
            if (dfn[u] == -1) dfs1(u, -1), stk.clear();
    }
};

void solve() {
    int n, m, u, v;
    cin >> n >> m;
    Tarjan<int> T(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        T.add_edge(u - 1, v - 1);
    }
    T.run();
    
    LL ans = 0;
    vector<bool> vis(n, false);
    for (int i = 0; i < n; i++) {
        if (vis[i]) continue;
        vis[i] = true;
        queue<int> q;
        q.push(i);
        int comp_sz = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            comp_sz++;
            for (auto v : T.g[u]) {
                if (vis[v]) continue;
                vis[v] = true;
                q.push(v);
            }
        }
        if (comp_sz < 2) continue;
        auto dfs = [&](this auto&& dfs, int u, int fa) -> int {
            int sz = (u < n) ? 1 : 0;
            for (auto v : T.bct[u]) {
                if (v == fa) continue;
                int sz_v = dfs(v, u);
                ans += 2LL * T.weights[u] * sz_v * sz;
                sz += sz_v;
            }
            ans += 2LL * T.weights[u] * sz * (comp_sz - sz);
            return sz;
        };
        dfs(i, -1);
    }
    cout << ans << endl;
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
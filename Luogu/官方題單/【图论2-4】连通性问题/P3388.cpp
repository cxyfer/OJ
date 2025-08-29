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
    vector<bool> cut_vertices;

    Tarjan(int n) : n(n) {
        g.resize(n);
        dfn.assign(n, -1);
        low.assign(n, -1);
        cut_vertices.assign(n, false);
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
                if (fa != -1 && low[v] >= dfn[u])  // cut vertex
                    cut_vertices[u] = true;
            }
        }
        if (fa == -1 && cnt > 1)  // cut vertex of root
            cut_vertices[u] = true;
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
    vector<int> ans;
    for (int u = 0; u < n; u++)
        if (T.cut_vertices[u]) ans.push_back(u + 1);
    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++)
        cout << ans[i] << " \n"[i == ans.size() - 1];
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
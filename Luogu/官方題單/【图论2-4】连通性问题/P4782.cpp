/*
P4782 【模板】2-SAT
https://www.luogu.com.cn/problem/P4782

將 (xi == x) or (xj == y) 轉換為：
1. NOT (xi == x) => (xj == y)
2. NOT (xj == y) => (xi == x)

在 c1: x_i 為假 (i) 和 c2: x_i 為真 (i + n) 中，優先選擇 scc_id 小，即拓撲序靠後的狀態。
假設存在一條由 SCC(i + n) 到 SCC(i) 的路徑，這意味著如果選擇 c2，那麼將選擇一系列狀態，最終必須選擇 c1，這顯然是矛盾的。
也就是說，在縮點後的樹上，如果存在一條由 c2 到 c1 的路徑，那麼在 c1 和 c2 中，我們只能選擇 c1，反之亦然。
而判定是否存在一條由 SCC(c2) 到 SCC(c1) 的路徑可以由拓樸序來判定，
拓樸排序後，SCC(c1) 的拓樸序一定比 SCC(c2) 還要靠後，因此若兩點間存在一條有向路徑，則拓樸序靠後的點必是終點。
在 Tarjan 中，由於添加到 SCCs 的過程是在「歸」的時候發生的，因此添加的順序是逆拓樸序，故 scc_id 越小，拓樸序越大。
故選擇 scc_id 小的狀態，即拓樸序靠後的狀態，可以保證不選擇到矛盾的狀態。
*/
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
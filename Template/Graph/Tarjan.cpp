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
    vector<bool> cut_vertices;

    /* 圓方樹 (Block-Cut Tree) 相關 */
    int bct_sz;
    vector<vector<T>> bct;
    vector<T> weights;

    Tarjan(int n) : n(n) {
        g.resize(n);
        dfn.assign(n, -1);
        low.assign(n, -1);
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
                if (low[v] > dfn[u])  // bridge
                    bridges.insert({min(u, v), max(u, v)});
                if (fa != -1 && low[v] >= dfn[u])  // cut vertex
                    cut_vertices[u] = true;
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
        if (fa == -1 && cnt > 1)  // cut vertex of root
            cut_vertices[u] = true;
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
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class UnionFind {
public:
    vector<int> fa, sz;
    UnionFind(int n) : fa(n), sz(n) {
        iota(fa.begin(), fa.end(), 0);
        fill(sz.begin(), sz.end(), 1);
    }

    int find(int x) {
        return fa[x] == x ? x : fa[x] = find(fa[x]);
    }

    bool merge(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return false;
        if (sz[fx] < sz[fy]) swap(fx, fy);
        fa[fy] = fx;
        sz[fx] += sz[fy];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, k, u, v;
    cin >> n >> m;
    UnionFind uf(n);
    vector<vector<int>> g(n);
    while (m--) {
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    cin >> k;
    int cnt = n - k; // 在最後，反抗軍只有 n - k 個星球
    vector<int> K(k);
    vector<bool> vis(n);
    for (int i = 0; i < k; ++i) {
        cin >> K[i];
        vis[K[i]] = true; // 標記會被帝國軍摧毀的星球
    }
    // 先將反抗軍剩下的星球連通
    for (int u = 0; u < n; ++u) {
        if (vis[u]) continue;
        for (int v : g[u]) {
            if (vis[v]) continue;
            if (uf.merge(u, v)) cnt--;
        }
    }
    // 倒序計算
    vector<int> ans(k);
    for (int i = k - 1; i >= 0; --i) {
        ans[i] = cnt;
        vis[K[i]] = false; // 時光倒流，將帝國軍摧毀的星球恢復
        cnt++; // 反抗軍又多了一個星球
        for (int v : g[K[i]]) {
            if (vis[v]) continue; // 跳過已經被摧毀的星球
            if (uf.merge(K[i], v)) cnt--;
        }
    }
    cout << cnt << endl; // 反抗軍最初有 cnt 個連通分量
    for (int i = 0; i < k; ++i) {
        cout << ans[i] << endl;
    }
    return 0;
}
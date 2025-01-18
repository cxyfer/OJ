#include <bits/stdc++.h>
using namespace std;
using LL = long long;
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
    int n, m, w, u, v;
    cin >> n >> m >> w;
    vector<int> C(n), D(n);
    for (int i = 0; i < n; i++) cin >> C[i] >> D[i];
    UnionFind uf(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        u--; v--;
        uf.merge(u, v);
    }
    vector<LL> cost(n), value(n);
    for (int i = 0; i < n; i++) {
        cost[uf.find(i)] += C[i];
        value[uf.find(i)] += D[i];
    }
    vector<LL> dp(w + 1, 0);
    for (int i = 0; i < n; i++) {
        if (cost[i] == 0 && value[i] == 0) continue;
        for (int j = w; j >= cost[i]; j--) {
            dp[j] = max(dp[j], dp[j - cost[i]] + value[i]);
        }
    }
    cout << dp[w] << endl;
    return 0;
}
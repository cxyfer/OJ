#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Edge {
    int u, v, w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

class UnionFind {
public:
    int cnt;
    vector<int> fa, sz;
    UnionFind(int n) : fa(n), sz(n), cnt(n) {
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
        cnt--;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v, w;
    cin >> n >> m;
    UnionFind uf(n);
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        edges[i].u--, edges[i].v--;
    }
    sort(edges.begin(), edges.end());
    int ans = 0;
    for (const auto& edge : edges) {
        if (uf.merge(edge.u, edge.v)) ans = edge.w;
        if (uf.cnt == 1) break;
    }
    cout << n - 1 << ' ' << ans << endl;
    return 0;
}
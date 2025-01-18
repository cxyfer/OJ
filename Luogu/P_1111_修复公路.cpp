#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class Edge {
public:
    int u, v, w;
    bool operator<(const Edge &other) const {
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
    vector<Edge> edges(m);
    UnionFind uf(n);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        edges[i].u--; edges[i].v--;
    }
    int ans = 0;
    sort(edges.begin(), edges.end());
    for (auto &e : edges) {
        if (uf.merge(e.u, e.v)) {
            ans = e.w;
        }
        if (uf.cnt == 1) break;
    }
    if (uf.cnt != 1) ans = -1;
    cout << ans << endl;
    return 0;
}
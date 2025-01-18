#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

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
    int m, n, k, u, v;
    cin >> m >> n >> k;
    UnionFind uf(m * n);
    for (int i = 0; i < k; i++) {
        cin >> u >> v;
        u--, v--;
        uf.merge(u, v);
    }
    cout << uf.cnt << endl;
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
#define endl '\n'

class UnionFind {
public:
    vector<int> pa, sz;
    UnionFind(int n) : sz(n, 1), pa(n) {
        iota(pa.begin(), pa.end(), 0);
    }

    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }

    void merge(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return;
        if (sz[fx] > sz[fy]) swap(fx, fy);
        pa[fx] = fy;
        sz[fy] += sz[fx];
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    UnionFind uf(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        uf.merge(u - 1, v - 1);
    }
    vector<int> arr;
    vector<bool> vis(n);
    for (int i = 0; i < n; i++) {
        int fx = uf.find(i);
        if (vis[fx]) continue;
        vis[fx] = true;
        arr.push_back(uf.sz[fx]);
    }
    bitset<N> f;
    f.set(0);
    for (int x : arr) {
        f |= f << x;
    }
    for (int i = 1; i <= n; i++) cout << f[i];
    cout << endl;
    return 0;
}
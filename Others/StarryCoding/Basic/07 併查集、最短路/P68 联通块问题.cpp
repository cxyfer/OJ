#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class UnionFind {
public:
    vector<int> fa, sz;
    int cnt;
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
        --cnt;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    UnionFind uf(n);
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        uf.merge(x - 1, y - 1);
    }
    vector<int> ans;
    vector<bool> vis(n);
    for (int i = 0; i < n; ++i) {
        int fx = uf.find(i);
        if (!vis[fx]) {
            vis[fx] = true;
            ans.push_back(uf.sz[fx]);
        }
    }
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); ++i) {
        cout << ans[i] << " ";
    }
    cout << endl;
    return 0;
}
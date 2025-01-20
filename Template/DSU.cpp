#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class UnionFind {
public:
    vector<int> pa, sz;
    int cnt;
    UnionFind(int n) {
        pa.resize(n);
        iota(pa.begin(), pa.end(), 0);
        sz.assign(n, 1);
        cnt = n;
    }
    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }
    bool unionSet(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) return false;
        if (sz[x] < sz[y]) swap(x, y);
        pa[y] = x;
        sz[x] += sz[y];
        cnt--;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m; cin >> n >> m;
    UnionFind uf(n);
    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        uf.unionSet(a-1, b-1);
    }
    bool visited[n] = {false};
    int ans = -m;
    for (int i = 0; i < n; i++) {
        int pa = uf.find(i);
        if (!visited[pa]) {
            visited[pa] = true;
            ans += uf.sz[pa] * (uf.sz[pa] - 1) / 2;
        }
    }
    cout << ans << endl;

    return 0;
}
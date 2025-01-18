#include <bits/stdc++.h>
using namespace std;
using LL = long long;
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
    char op;
    int n, m, u, v;
    cin >> n;
    cin >> m;
    UnionFind uf(n);
    vector<vector<bool>> is_enemy(n, vector<bool>(n, false));
    while (m--) {
        cin >> op >> u >> v;
        u--; v--;
        if (op == 'F') {
            uf.merge(u, v);
        }
        else {
            is_enemy[u][v] = is_enemy[v][u] = true;
            for (int i = 0; i < n; i++) {
                if (i == u || i == v) continue;
                if (is_enemy[u][i]) uf.merge(v, i);
                if (is_enemy[v][i]) uf.merge(u, i);
            }
        }
    }
    cout << uf.cnt << endl;
    return 0;
}
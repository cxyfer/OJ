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
    char op;
    int n, q, u, v;
    cin >> n >> q;
    UnionFind uf(n * 2);
    while (q--) {
        cin >> op >> u >> v;
        u--; v--;
        if (op == 'A') { // 兩個電荷互相吸引，標記為不同電荷
            uf.merge(u, v + n);
            uf.merge(u + n, v);
        } else if (op == 'R') { // 兩個電荷互相排斥，標記為相同電荷
            uf.merge(u, v);
            uf.merge(u + n, v + n);
        } else {
            bool flag1 = (uf.find(u) == uf.find(v) && uf.find(u + n) == uf.find(v + n));
            bool flag2 = (uf.find(u) == uf.find(v + n) && uf.find(u + n) == uf.find(v));
            if (!flag1 && flag2) cout << "A" << endl;
            else if (flag1 && !flag2) cout << "R" << endl;
            else cout << "?" << endl;
        }
    }
    return 0;
}
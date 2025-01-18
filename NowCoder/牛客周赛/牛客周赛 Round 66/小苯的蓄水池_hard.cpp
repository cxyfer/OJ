#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

class UnionFind {
    vector<LL> pa, sz, tot;
public:
    UnionFind(int n, vector<LL>& nums): pa(n), sz(n, 1), tot(nums) {
        iota(pa.begin(), pa.end(), 0);
    }

    LL find(int x) {
        if (pa[x] != x) pa[x] = find(pa[x]);
        return pa[x];
    }

    void merge(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return;
        if (fx < fy) swap(fx, fy);
        pa[fy] = fx;
        sz[fx] += sz[fy];
        tot[fx] += tot[fy];
    }

    double get(int x) {
        return 1.0 * tot[find(x)] / sz[find(x)];
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, op, l, r, idx;
    cin >> n >> m;
    vector<LL> A(n + 1);
    for (int i = 1; i <= n; ++i) cin >> A[i];
    UnionFind uf(n + 1, A);
    for (int i = 0; i < m; ++i) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r;
            idx = uf.find(l);
            while (idx < r) {
                uf.merge(idx, idx + 1);
                idx = uf.find(idx);
            }
        } else {
            cin >> idx;
            cout << fixed << setprecision(10) << uf.get(idx) << endl;
        }
    }
    return 0;
}
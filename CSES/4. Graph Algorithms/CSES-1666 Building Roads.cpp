#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class UnionFind {
public:
    vector<int> pa, sz;
    UnionFind(int n) : pa(n), sz(n, 1) {
        iota(pa.begin(), pa.end(), 0);
    }

    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }

    bool merge(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return false;
        if (sz[fx] < sz[fy]) swap(fx, fy);
        pa[fy] = fx;
        sz[fx] += sz[fy];
        return true;
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
    for (int i = 0; i < n; i++) {
        if (uf.find(i) == i) {
            arr.push_back(i);
        }
    }
    cout << arr.size() - 1 << endl;
    for (int i = 1; i < arr.size(); i++) {
        cout << arr[i - 1] + 1 << " " << arr[i] + 1 << endl;

    }
    return 0;
}
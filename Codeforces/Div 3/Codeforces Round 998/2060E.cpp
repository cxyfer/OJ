#include <bits/stdc++.h>
using namespace std;
using LL = long long;
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
        while (pa[x] != x) {
            pa[x] = pa[pa[x]];
            x = pa[x];
        }
        return x;
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
    int t, n, m1, m2;
    cin >> t;
    while (t--) {
        cin >> n >> m1 >> m2;
        vector<pair<int,int>> edges1(m1), edges2(m2);
        for (auto& [u, v] : edges1) {
            cin >> u >> v;
            u--, v--;
        }
        for (auto& [u, v] : edges2) {
            cin >> u >> v;
            u--, v--;
        }

        LL ans = 0;
        UnionFind uf1(n), uf2(n);
        for (auto [u, v] : edges2) {
            uf2.unionSet(u, v);
        }
        for (auto [u, v] : edges1) {
            if (uf2.find(u) != uf2.find(v)) {
                ans++;
            } else {
                uf1.unionSet(u, v);
            }
        }

        vector<pair<int,int>> pairs(n);
        for (int i = 0; i < n; i++) {
            pairs[i] = {uf2.find(i), uf1.find(i)};
        }
        sort(pairs.begin(), pairs.end());

        int i = 0;
        while (i < n) {
            int cnt = 1;
            int prev1 = pairs[i].second;
            int curr2 = pairs[i].first;
            i++;
            while (i < n && pairs[i].first == curr2) {
                if (pairs[i].second != prev1) {
                    cnt++;
                    prev1 = pairs[i].second;
                }
                i++;
            }
            if (cnt > 1) {
                ans += (cnt - 1);
            }
        }
        cout << ans << endl;
    }
    return 0;
}

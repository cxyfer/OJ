#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

/* 
    種類併查集
*/

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
    int n, m, op, x, y;
    cin >> n >> m;
    UnionFind uf(n * 3); // 同類、獵物、天敵
    int ans = 0;
    while (m--) {
        cin >> op >> x >> y;
        x--; y--;
        // 超出範圍一定是假話
        if (x >= n || y >= n) {
            ans++;
            continue;
        }
        // x 和 y 是同類
        if (op == 1) { 
            // 若 x 是 y 的天敵、或 x 是 y 的獵物，則是假話
            if (uf.find(x) == uf.find(y + n) || uf.find(x) == uf.find(y + 2 * n)) ans++;
            else {
                uf.merge(x, y);
                uf.merge(x + n, y + n);
                uf.merge(x + 2 * n, y + 2 * n);
            }
        }
        // x 吃 y，表示 x 是 y 的天敵
        else { 
            // 若 x 和 y 是同類、或 x 是 y 的獵物，則是假話
            if (uf.find(x) == uf.find(y) || uf.find(x) == uf.find(y + 2 * n)) ans++;
            else {
                uf.merge(x, y + n);
                uf.merge(x + n, y + 2 * n);
                uf.merge(x + 2 * n, y);
            }
        }
    }
    cout << ans << endl;
    return 0;
}
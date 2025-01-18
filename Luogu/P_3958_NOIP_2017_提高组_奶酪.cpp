#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct Node {
    int x, y, z;
};

LL dis2(Node& a, Node& b) {
    LL dx = a.x - b.x, dy = a.y - b.y, dz = a.z - b.z;
    return dx * dx + dy * dy + dz * dz;
}

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
    int t, n, h, r;
    cin >> t;
    while (t--) {
        cin >> n >> h >> r;
        vector<Node> nodes(n + 1);
        for (int i = 1; i <= n; i++) {
            cin >> nodes[i].x >> nodes[i].y >> nodes[i].z;
        }
        UnionFind uf(n + 2); // 0 表示下表面，n + 1 表示上表面
        // 枚舉所有點對，檢查兩兩是否相連
        for (int i = 1; i <= n; i++) {
            if (nodes[i].z - r <= 0) uf.merge(i, 0);
            if (nodes[i].z + r >= h) uf.merge(i, n + 1);
            for (int j = 1; j < i; j++) {
                if (dis2(nodes[i], nodes[j]) <= 4LL * r * r) uf.merge(i, j);
            }
        }
        cout << (uf.find(0) == uf.find(n + 1) ? "Yes" : "No") << endl;
    }
    return 0;
}
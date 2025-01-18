#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

class UnionFind {
public:
    vector<int> pa, sz;
    int cnt;

    UnionFind(int n) : pa(n), sz(n, 1), cnt(n) {
        iota(pa.begin(), pa.end(), 0);
    }

    int find(int x) {
        if (pa[x] != x) {
            pa[x] = find(pa[x]);
        }
        return pa[x];
    }

    bool _union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (sz[px] < sz[py]) {
            swap(px, py);
        }
        pa[py] = px;
        sz[px] += sz[py];
        cnt--;
        return true;
    }

    UnionFind& operator=(const UnionFind& other) {
        if (this != &other) {
            pa = other.pa;
            sz = other.sz;
            cnt = other.cnt;
        }
        return *this;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, s;
    cin >> n >> m >> s;
    LL tot = 0;
    vector<int> deg(n + 1);
    UnionFind uf0(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        deg[u]++;
        deg[v]++;
        tot += abs(u - v);
        uf0._union(u, v);
    }
    for (int i = 1; i <= n; ++i) {
        // 複製，避免修改到原始的 uf0 和 tot
        UnionFind uf = uf0;
        LL ans = tot;
        // 在起點 s 和終點 i 連邊
        deg[s]++;
        deg[i]++;

        // 連接奇數度的頂點
        vector<int> odds;
        for (int u = 1; u <= n; ++u) {
            if (deg[u] & 1) odds.push_back(u);
        }
        for (int j = 0; j < odds.size(); j += 2) {
            // 連接 (x, y) 邊的 cost 等同連接 (x, x + 1), (x + 1, x + 2), ... , (y - 1, y) 的邊
            // 但後者可以使更多頂點連通
            int x = odds[j], y = odds[j + 1];
            for (int k = x; k < y; ++k) {
                uf._union(k, k + 1);
            }
            ans += y - x;
        }

        // 檢查所有需要連接的頂點是否已經連通
        // 若兩個連通分量不連通，則應該考慮連接第一個連通分量最大頂點和第二個連通分量最小頂點
        vector<int> nodes;
        for (int u = 1; u <= n; ++u) {
            if (deg[u]) nodes.push_back(u);
        }
        vector<pair<int, int>> edges;
        for (int j = 0; j < nodes.size() - 1; ++j) {
            int x = nodes[j], y = nodes[j + 1];
            if (uf.find(x) != uf.find(y)) { // 不連通
                edges.emplace_back(x, y);
            }
        }
        // 按照邊的 cost 排序，類似 Kruskal 算法
        sort(edges.begin(), edges.end(), [](const auto& a, const auto& b) {
            return a.second - a.first < b.second - b.first;
        });
        for (const auto& [x, y] : edges) {
            if (uf._union(x, y)) { // 連通這條邊兩側的兩個連通分量
                ans += (y - x) << 1; // 訪問完 y 所屬的連通分量後，要回到 x 所屬的連通分量，故 cost 要乘以 2
            }
        }
        // 輸出並恢復起點和終點的度數
        cout << ans << ' ';
        deg[s]--;
        deg[i]--;
    }
    return 0;
}
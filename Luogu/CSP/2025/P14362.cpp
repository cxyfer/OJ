/*
"""
P14362 [CSP-S 2025] 道路修复 / road（官方数据）
https://www.luogu.com.cn/problem/P14362

MST

給定一個 n 個城市 k 個鄉鎮的圖，城市之間有 m 條道路，
且每個鄉鎮都和所有城市相連，但啟用鄉鎮需要額外的代價。
求使所有城市連通的最小代價。

注意到 k <= 10，這暗示我們可以二進位枚舉所有的鄉鎮狀態。
在原圖中只有 MST 上的邊需要考慮，因此我們可以先求出 MST，這樣可以把 m 減少到 n - 1

對於枚舉的狀態可以把啟用的鄉鎮相鄰的邊加入再求一次 MST，但瓶頸在每次都需要重新排序。
因此可以直接把所有邊都加入，然後只選擇啟用的鄉鎮相鄰的邊，這樣可以避免重新排序。

第一次MST需要 O(m log m) 的時間
排序 (n - 1) + kn 條邊需要 kn log kn 的時間
枚舉狀態需要 2^k 次，每次需要 O(kn) 的時間來計算當前狀態的 MST
總時間複雜度為 O(m log m + kn log kn + 2^k * kn)
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

class UnionFind {
public:
    vector<int> pa, sz;
    UnionFind(int n) {
        pa.resize(n);
        iota(pa.begin(), pa.end(), 0);
        sz.assign(n, 1);
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
        return true;
    }
};

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<array<int, 3>> edges(m);
    for (auto& [u, v, w] : edges) cin >> u >> v >> w;
    sort(edges.begin(), edges.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
        return a[2] < b[2];
    });

    UnionFind uf(n + 1);
    int idx = 0;
    for (auto& [u, v, w] : edges) {
        if (uf.unionSet(u, v)) {
            edges[idx++] = {u, v, w};
            if (idx == n - 1) break;
        }
    }
    edges.erase(edges.begin() + idx, edges.end());
    LL ans = accumulate(edges.begin(), edges.end(), 0LL, [](LL sum, const array<int, 3>& e) {
        return sum + e[2];
    });

    vector<int> cost(k + 1);
    for (int j = 1; j <= k; j++) {
        cin >> cost[j];
        for (int i = 1; i <= n; i++) {
            int w;
            cin >> w;
            edges.push_back({i, n + j, w});
        }
    }
    sort(edges.begin(), edges.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
        return a[2] < b[2];
    });

    for (int msk = 1; msk < (1 << k); msk++) {
        LL cur = 0;
        vector<bool> vis(k + 1);
        for (int i = 0; i < k; i++) {
            if (msk & (1 << i)) {
                cur += cost[i + 1];
                vis[i + 1] = true;
            }
        }

        UnionFind uf(n + k + 1);
        int idx = 0;
        int tgt = n + __builtin_popcount(msk);
        for (auto& [u, v, w] : edges) {
            if (v > n && !vis[v - n]) continue;
            if (uf.unionSet(u, v)) {
                cur += w;
                idx++;
                if (idx == tgt) break;
            }
        }
        ans = min(ans, cur);
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}
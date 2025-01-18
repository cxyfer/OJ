#include <bits/stdc++.h>
using namespace std;
const int N = 128;
#define endl '\n'

// Disjoint Set Union 用於判斷圖是否連通
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
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    char u, v;
    cin >> n;
    map<char, int> deg;
    map<char, vector<pair<char, int>>> g;
    UnionFind uf(N);
    for (int idx = 0; idx < n; idx++) {
        cin >> u >> v;
        g[u].push_back({v, idx});
        g[v].push_back({u, idx});
        deg[u]++;
        deg[v]++;
        uf._union(u, v);
    }
    // 將邊 (u, v) 按 v ASCII 序由大到小排序
    for (auto &[u, vec] : g) {
        sort(vec.begin(), vec.end(), [](const auto &a, const auto &b) {
            return a.first > b.first;
        });
    }

    int odd_cnt = 0; // 奇數度節點數
    char st = 0; // 起點
    for (auto &[u, val] : deg) {
        if (val & 1) {
            if (!st) st = u;
            odd_cnt++;
        }
    }
    if (!st) {
        st = g.begin()->first;
    }

    // Hierholzer's Algorithm 找 Eulerian Path
    string path;
    vector<bool> used(n); // 記錄邊 idx 是否被使用過
    auto dfs = [&](auto &&dfs, char u) -> void {
        while (!g[u].empty()) {
            auto [v, idx] = g[u].back();
            g[u].pop_back();
            if (used[idx]) continue;
            used[idx] = true;
            dfs(dfs, v);
        }
        path += u;
    };
    dfs(dfs, st);

    // 判斷圖是否連通
    char root = (path.empty()) ? 0 : uf.find(path[0]);
    bool is_connected = true;
    for (auto &[u, vec] : g) {
        if (uf.find(u) != root) {
            is_connected = false;
            break;
        }
    }

    // 判斷是否存在歐拉路徑
    if ((odd_cnt == 0 || odd_cnt == 2) && path.size() == n + 1 && is_connected) {
        reverse(path.begin(), path.end());
        cout << path;
    } else {
        cout << "No Solution";
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v;
    cin >> n >> m;
    vector<int> deg(n, 0);
    vector<vector<pair<int, int>>> g(n);
    for (int idx = 0; idx < m; idx++) {
        cin >> u >> v;
        u--, v--;
        g[u].push_back({v, idx});
        deg[u]++;
        deg[v]--;
    }

    // 將邊 (u, v) 按 v 由大到小排序
    for (int u = 0; u < n; u++) {
        sort(g[u].begin(), g[u].end(), greater<pair<int, int>>());
    }

    // 找起點
    int st = -1;
    int cnt0 = 0, cnt_p1 = 0, cnt_m1 = 0;
    for (int u = 0; u < n; u++) {
        if (deg[u] == 0) cnt0++;
        else if (deg[u] == 1) cnt_p1++, st = u;
        else if (deg[u] == -1) cnt_m1++;
    }
    if (st == -1) st = 0;

    bool is_eulerian = (cnt0 == n && cnt_p1 == 0 && cnt_m1 == 0) || 
                      (cnt0 == n - 2 && cnt_p1 == 1 && cnt_m1 == 1);
    if (!is_eulerian) {
        cout << "No" << endl;
        return 0;
    }

    // Hierholzer's Algorithm 找 Eulerian Path
    vector<int> path;
    vector<bool> used(m); // 記錄邊 idx 是否被使用過
    auto dfs = [&](auto &&dfs, int u) -> void {
        while (!g[u].empty()) {
            auto [v, idx] = g[u].back();
            g[u].pop_back();
            if (used[idx]) continue;
            used[idx] = true;
            dfs(dfs, v);
        }
        path.push_back(u + 1);
    };
    dfs(dfs, st);

    // 判斷是否存在歐拉路徑
    if (path.size() == m + 1) {
        reverse(path.begin(), path.end());
        for (int i = 0; i < path.size(); i++) {
            cout << path[i] << (i != path.size() - 1 ? ' ' : endl);
        }
    } else {
        cout << "No";
    }
    return 0;
}
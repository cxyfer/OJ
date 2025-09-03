#include <bits/stdc++.h>
using namespace std;
const int N = 5e4 + 5;
#define endl '\n'

/*
由於每個點最多只有一條出邊，因此只會有以下兩種情況
1. 洽好形成一個或多個環，沒有節點入度為0，用普通 DFS 計算即可
2. 內向基環樹，有若干個入度為0的節點，計算這些點到環的距離哪個最大即可
Case 1 也可以視為內向基環樹的一種，可以一起處理

ZeroJudge 上面的數據不夠強，沒有以下幾種情況：
- 基環樹的樹上有分支
- 有多棵內向基環樹

類題：
- 2127. Maximum Employees to Be Invited to a Meeting 
*/

// 反向圖上 DFS 計算最長鏈長度，以及該條鏈上的葉子節點
pair<int, int> rdfs(int u, vector<vector<int>> &rg) {
    int res = 0, idx = u;
    for (int v : rg[u]) {
        auto [cnt, i] = rdfs(v, rg);
        if (res < cnt or (res == cnt and idx > i)) {
            res = cnt;
            idx = i;
        }
    }
    return {res + 1, idx};
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, u, v, kase = 1;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> g(n + 1), ind(n + 1);
        for (int i = 0; i < n; ++i) {
            cin >> u >> v;
            g[u] = v;
            ind[v]++;
        }
        int ans = 0, mx = 0;
        // 使用拓撲排序建不包含基環的反向圖
        vector<vector<int>> rg(n + 1);
        queue<int> q;
        for (int u = 1; u <= n; ++u) {
            if (ind[u] == 0) q.push(u);
        }
        while (!q.empty()) { // Topological Sort
            int u = q.front(); q.pop();
            int v = g[u];
            rg[v].push_back(u);
            ind[v]--;
            if (ind[v] == 0) q.push(v);
        }
        // 遍歷基環，注意可能有多個基環
        for (int u = 1; u <= n; ++u) {
            // 略過非基環上的點，或已經訪問過的基環
            if (ind[u] == 0) continue; 
            // 找到該基環上的所有點
            vector<int> rings = {u};
            int v = g[u];
            while (v != u) {
                rings.push_back(v);
                v = g[v];
            }
            // 計算以 v 為根節點的最大鏈長度，以及該條鏈上的葉子節點
            int max_len = 0, idx = -1;
            for (int v : rings) {
                ind[v] = 0; // 清空入度，避免重複訪問
                auto [cur_len, leaf] = rdfs(v, rg);
                if (cur_len > max_len || (cur_len == max_len && leaf < idx)) {
                    max_len = cur_len, idx = leaf;
                }
            }
            // 最大鏈長度加上基環的長度即為此顆基環樹能獲得的答案
            max_len += rings.size() - 1; // 減去位於基環上的根節點
            if (mx < max_len || (mx == max_len && ans > idx)) {
                mx = max_len, ans = idx;
            }
        }
        cout << "Case " << kase++ << ": " << ans << endl;
    }
    return 0;
}
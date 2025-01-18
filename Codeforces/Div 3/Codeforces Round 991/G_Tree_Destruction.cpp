/*
考慮以下兩種 Case
1. a = b，則會產生 len(g[a]) 個連通分量
2. a != b，則會產生一條路徑。對於路徑上的每一點 u：
  - 如果 u 在路徑中，則會產生 len(g[u]) - 2 個連通分量
  - 如果 u 是路徑的端點，則會產生 len(g[u]) - 1 個連通分量
  由於路徑一定有兩個端點，因此可以皆視為 len(g[u]) - 2 ，最後再 + 2 即可。

對於 Case 1，直接取 max(len(g[u])) 即可，但其實也可以視為 Case 2 的特例。
對於 Case 2，則約等同求樹上最長直徑，使用樹形 DP 維護子樹中最大及次大鏈值即可。
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, u, v;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<vector<int>> g(n);
        for (int i = 0; i < n - 1; ++i) {
            cin >> u >> v;
            u--, v--;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        int ans = 0;
        // Case 1, can be ignored
        for (int i = 0; i < n; ++i) {
            ans = max(ans, (int) g[i].size());
        }
        // Case 2
        auto dfs = [&](auto &&dfs, int u, int fa) -> int {
            int first = 0, second = 0; // 最大及次大鏈值
            int cur = (int) g[u].size() - 2; // 當前節點值
            for (int v : g[u]) {
                if (v == fa) continue;
                int t = dfs(dfs, v, u);
                if (t > first) {
                    second = first;
                    first = t;
                } else if (t > second) {
                    second = t;
                }
            }
            ans = max(ans, first + second + cur + 2); // 更新答案
            return first + cur; // 返回該子樹的最大鏈值
        };
        dfs(dfs, 0, -1);
        cout << ans << endl;
    }
    return 0;
}
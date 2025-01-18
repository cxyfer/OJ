/*
 * @lc app=leetcode.cn id=2101 lang=cpp
 *
 * [2101] 引爆最多的炸弹
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    1. DFS
    2. Bitset + Floyd-Warshall
*/
class Solution1 {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        vector<vector<int>> g(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (pow(bombs[i][0] - bombs[j][0], 2) + pow(bombs[i][1] - bombs[j][1], 2) <= pow(bombs[i][2], 2)) {
                    g[i].push_back(j);
                }
            }
        }

        vector<bool> vis(n, false);
        function<int(int)> dfs = [&](int i) {
            vis[i] = true;
            int res = 1;
            for (int j : g[i]) {
                if (!vis[j]) res += dfs(j);
            }
            return res;
        };

        int ans = 0;
        for (int i = 0; i < n; i++) {
            vis.assign(n, false);
            ans = max(ans, dfs(i));
        }
        return ans;
    }
};

class Solution2 {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        vector<bitset<100>> dp(n); // n <= 100
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (pow(bombs[i][0] - bombs[j][0], 2) + pow(bombs[i][1] - bombs[j][1], 2) <= pow(bombs[i][2], 2)) {
                    dp[i].set(j);
                }
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (dp[i].test(k)) { // 如果 i 可以到達 k ，則 i 可以到達 k 可到達的所有點 
                    dp[i] |= dp[k];
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(ans, (int) dp[i].count());
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end
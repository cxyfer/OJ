/*
 * @lc app=leetcode.cn id=2959 lang=cpp
 *
 * [2959] 关闭分部的可行集合数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    Bitmask + Floyd Warshall
*/
class Solution {
public:
    int numberOfSets(int n, int maxDistance, vector<vector<int>>& roads) {
        // Build graph
        vector<vector<int>> g(n, vector<int>(n, INT_MAX / 2));
        for (int i = 0; i < n; i++) g[i][i] = 0;
        for (auto& r : roads) {
            g[r[0]][r[1]] = min(g[r[0]][r[1]], r[2]);
            g[r[1]][r[0]] = min(g[r[1]][r[0]], r[2]);
        }
        int ans = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            // Subgraph
            vector<vector<int>> g2(n);
            for (int i = 0; i < n; i++) {
                if (mask >> i & 1) g2[i] = g[i];
            }
            // Floyd Warshall
            for (int k = 0; k < n; k++) {
                if (!(mask >> k & 1)) continue;
                for (int i = 0; i < n; i++) {
                    if (!(mask >> i & 1)) continue;
                    for (int j = 0; j < n; j++) {
                        if (g2[i][k] + g2[k][j] < g2[i][j]) {
                            g2[i][j] = g2[i][k] + g2[k][j];
                        }
                    }
                }
            }
            // Check
            bool flag = true;
            for (int i = 0; i < n && flag; i++) {
                if (!(mask >> i & 1)) continue;
                for (int j = 0; j < n && flag; j++) {
                    if (!(mask >> j & 1)) continue;
                    if (g2[i][j] > maxDistance) flag = false;
                }
            }
            ans += flag;
        }
        return ans;
    }
};
// @lc code=end
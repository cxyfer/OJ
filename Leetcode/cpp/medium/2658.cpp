/*
 * @lc app=leetcode.cn id=2658 lang=cpp
 *
 * [2658] 网格图中鱼的最大数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findMaxFish(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int ans = 0;
        vector<pair<int, int>> dirs{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        auto dfs = [&](auto &&dfs, int x, int y) -> int {
            int res = grid[x][y];
            grid[x][y] = 0;
            for (auto [dx, dy] : dirs) {
                int nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny]) {
                    res += dfs(dfs, nx, ny);
                }
            }
            return res;
        };
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) continue;
                ans = max(ans, dfs(dfs, i, j));
            }
        }
        return ans;
    }
};
// @lc code=end


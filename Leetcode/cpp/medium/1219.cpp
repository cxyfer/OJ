/*
 * @lc app=leetcode.cn id=1219 lang=cpp
 *
 * [1219] 黄金矿工
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int m, n;
    int DIR[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int dfs(vector<vector<int>>& grid, int x, int y) {
        int res = 0;
        int origin = grid[x][y]; // backup
        grid[x][y] = 0; // mark as visited
        for (int k = 0; k < 4; k++) {
            int nx = x + DIR[k][0], ny = y + DIR[k][1];
            if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] != 0) {
                res = max(res, dfs(grid, nx, ny));
            }
        }
        grid[x][y] = origin; // backtracking
        return res + origin;
    }
    int getMaximumGold(vector<vector<int>>& grid) {
        m = grid.size(), n = grid[0].size();
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) {
                    ans = max(ans, dfs(grid, i, j));
                }
            }
        }
        return ans;
    }
};
// @lc code=end


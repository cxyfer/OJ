/*
 * @lc app=leetcode.cn id=2257 lang=cpp
 * @lcpr version=30204
 *
 * [2257] 统计网格图中没有被保卫的格子数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<vector<int>> grid(m, vector<int>(n, -1));
        for (auto& g : guards) grid[g[0]][g[1]] = 1;
        for (auto& w : walls) grid[w[0]][w[1]] = 2;

        auto dfs = [&](auto &&dfs, int x, int y, int dx, int dy) -> void {
            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] != 1 && grid[x][y] != 2) {
                grid[x][y] = 3;
                dfs(dfs, x + dx, y + dy, dx, dy);
            }
        };
        for (auto& g : guards)
            for (auto [dx, dy] : dirs)
                dfs(dfs, g[0] + dx, g[1] + dy, dx, dy);
        
        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == -1)
                    ans++;
        return ans;
    }
};
// @lc code=end

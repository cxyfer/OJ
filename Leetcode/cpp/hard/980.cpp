/*
 * @lc app=leetcode.cn id=980 lang=cpp
 * @lcpr version=30204
 *
 * [980] 不同路径 III
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
vector<pair<int, int>> DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int tot = 0, sx = -1, sy = -1;
        for (auto [i, row] : views::enumerate(grid))
            for (auto [j, x] : views::enumerate(row))
                if (x == 1)
                    sx = i, sy = j;
                else
                    tot += (x == 0);
        int ans = 0, cnt = 0;
        auto dfs = [&](this auto&& dfs, int x, int y) -> void {
            if (grid[x][y] == 2) {
                ans += (cnt == tot + 1);
                return;
            }
            cnt++;
            grid[x][y] = -1;
            for (auto [dx, dy] : DIRS) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || grid[nx][ny] == -1)
                    continue;
                dfs(nx, ny);
            }
            cnt--;
            grid[x][y] = 0;
            return;
        };
        dfs(sx, sy);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,0,0,0],[0,0,0,0],[0,0,0,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,1],[2,0]]\n
// @lcpr case=end

 */


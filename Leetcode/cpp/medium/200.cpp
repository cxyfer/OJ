/*
 * @lc app=leetcode id=200 lang=cpp
 * @lcpr version=30122
 *
 * [200] Number of Islands
 */


// @lcpr-template-start
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution1 {
    const vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();

        auto dfs = [&](this auto&& dfs, int x, int y) -> void {
            for (auto [dx, dy] : dirs) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] == '0') continue;
                grid[nx][ny] = '0';
                dfs(nx, ny);
            }
        };

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0') continue;
                grid[i][j] = '0';
                dfs(i, j);
                ans++;
            }
        }
        return ans;
    }
};

class Solution2 {
    // 只需檢查右邊和下邊，避免重複合併
    const vector<pair<int, int>> dirs = {{1, 0}, {0, 1}};
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();

        vector<int> sz(m * n, 1);
        auto fa = ranges::iota_view(0, m * n) | ranges::to<vector<int>>();

        int ans = ranges::fold_left(grid, 0, [&](int acc, const auto& row) -> int {
            return acc + ranges::count(row, '1');
        });

        auto find = [&](this auto&& find, int x) -> int {
            return x == fa[x] ? x : fa[x] = find(fa[x]);
        };

        auto merge = [&](int x, int y) -> void {
            x = find(x), y = find(y);
            if (x == y) return;
            if (sz[x] < sz[y]) swap(x, y);
            fa[y] = x;
            sz[x] += sz[y];
            ans--;
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0') continue;
                for (auto [dx, dy] : dirs) {
                    int nx = i + dx, ny = j + dy;
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] == '0') continue;
                    merge(i * n + j, nx * n + ny);
                }
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
// @lcpr case=end

// @lcpr case=start
// [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
// @lcpr case=end

 */


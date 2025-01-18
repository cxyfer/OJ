/*
 * @lc app=leetcode.cn id=2373 lang=cpp
 *
 * [2373] 矩阵中的局部最大值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        for (int i = 0; i < n - 2; ++i){
            for (int j = 0; j < n - 2; ++j) {
                for (int x = i; x < i + 3; ++x) {
                    for (int y = j; y < j + 3; ++y) {
                        grid[i][j] = max(grid[i][j], grid[x][y]);
                    }
                }
            }
            grid[i].resize(n-2);
        }
        grid.resize(n-2);
        return grid;
    }
};
// @lc code=end


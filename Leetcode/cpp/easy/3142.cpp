/*
 * @lc app=leetcode.cn id=3142 lang=cpp
 *
 * [3142] Check if Grid Satisfies Conditions
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool satisfiesConditions(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i + 1 < m && grid[i][j] != grid[i+1][j]) return false;
                if (j + 1 < n && grid[i][j] == grid[i][j+1]) return false;
            }
        }
        return true;
    }
};
// @lc code=end

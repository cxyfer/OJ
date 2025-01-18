/*
 * @lc app=leetcode.cn id=3033 lang=cpp
 *
 * [3033] 修改矩阵
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> modifiedMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> mx(n, INT_MIN);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                mx[j] = max(mx[j], matrix[i][j]);
        vector<vector<int>> ans(m, vector<int>(n));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                ans[i][j] = (matrix[i][j] == -1) ? mx[j] : matrix[i][j];
        return ans;
    }
};
// @lc code=end
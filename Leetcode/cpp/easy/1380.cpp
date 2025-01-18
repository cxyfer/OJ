/*
 * @lc app=leetcode.cn id=1380 lang=cpp
 *
 * [1380] 矩阵中的幸运数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    1. 預處理，找出每一橫列的最小值和每一直行的最大值
    2. Lucky number 最多只會有一個
        如果存在，則一定是每一橫列中的最小值其中的最大值，檢查其是否為該直行的最大值即可
*/

class Solution1 {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> row_mn(m, INT_MAX), col_mx(n, INT_MIN);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row_mn[i] = min(row_mn[i], matrix[i][j]);
                col_mx[j] = max(col_mx[j], matrix[i][j]);
            }
        }
        vector<int> ans;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == row_mn[i] && matrix[i][j] == col_mx[j]) {
                    ans.push_back(matrix[i][j]);
                }
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int row_mx = -INT_MAX, idx = 0;
        for (auto& row : matrix) {
            auto it = min_element(row.begin(), row.end());
            if (*it > row_mx) {
                row_mx = *it;
                idx = it - row.begin();
            }
        }
        for (auto& row : matrix) {
            if (row[idx] > row_mx) {
                return {};
            }
        }
        return {row_mx};
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end
/*
 * @lc app=leetcode.cn id=118 lang=cpp
 * @lcpr version=30204
 *
 * [118] 杨辉三角
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans(numRows);
        for (int i = 0; i < numRows; i++) {
            ans[i].resize(i + 1);
            ans[i][0] = ans[i][i] = 1;
            for (int j = 1; j < i; j++) ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j];
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */


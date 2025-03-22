/*
 * @lc app=leetcode.cn id=2643 lang=cpp
 * @lcpr version=30204
 *
 * [2643] 一最多的行
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        int n = mat.size();
        vector<int> ans(2);
        for (int i = 0; i < n; i++) {
            auto& row = mat[i];
            int s = accumulate(row.begin(), row.end(), 0);
            if (s > ans[1]) ans = {i, s};
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[0,1],[1,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,0],[0,1,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0],[1,1],[0,0]]\n
// @lcpr case=end

 */


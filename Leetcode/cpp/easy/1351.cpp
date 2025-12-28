/*
 * @lc app=leetcode.cn id=1351 lang=cpp
 * @lcpr version=30204
 *
 * [1351] 统计有序矩阵中的负数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int ans = 0;
        for (auto& row : grid)
            ans += row.size() - (upper_bound(row.begin(), row.end(), 0, greater<int>()) - row.begin());
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,2],[1,0]]\n
// @lcpr case=end

 */


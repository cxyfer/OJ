/*
 * @lc app=leetcode.cn id=3701 lang=cpp
 * @lcpr version=30204
 *
 * [3701] 计算交替和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int alternatingSum(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < nums.size(); ++i)
            ans += (i & 1? -nums[i] : nums[i]);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,5,7]\n
// @lcpr case=end

// @lcpr case=start
// [100]\n
// @lcpr case=end

 */


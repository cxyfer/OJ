/*
 * @lc app=leetcode.cn id=3745 lang=cpp
 * @lcpr version=30204
 *
 * [3745] 三元素表达式的最大值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int maximizeExpressionOfThree(vector<int>& nums) {
        int n = nums.size();
        ranges::sort(nums);
        return nums[n - 1] + nums[n - 2] - nums[0];
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,4,2,5]\n
// @lcpr case=end

// @lcpr case=start
// [-2,0,5,-2,4]\n
// @lcpr case=end

 */


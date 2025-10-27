/*
 * @lc app=leetcode.cn id=3727 lang=cpp
 * @lcpr version=30204
 *
 * [3727] 最大交替平方和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        for (auto &x : nums) x *= x;
        nth_element(nums.begin(), nums.begin() + n/2, nums.end());
        return accumulate(nums.begin() + n/2, nums.end(), 0LL) - accumulate(nums.begin(), nums.begin() + n/2, 0LL);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,-1,2,-2,3,-3]\n
// @lcpr case=end

 */


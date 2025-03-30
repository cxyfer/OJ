/*
 * @lc app=leetcode.cn id=713 lang=cpp
 * @lcpr version=30204
 *
 * [713] 乘积小于 K 的子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int n = nums.size();
        if (k <= 1) return 0;
        int ans = 0, left = 0;
        long long prod = 1;
        for (int right = 0; right < n; ++right) {
            prod *= nums[right];
            while (prod >= k) prod /= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [10,5,2,6]\n100\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n0\n
// @lcpr case=end

 */


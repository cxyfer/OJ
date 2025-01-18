/*
 * @lc app=leetcode.cn id=213 lang=cpp
 *
 * [213] 打家劫舍 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int f1(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n + 1, 0);
        dp[1] = nums[0];
        for (int i = 2; i <= n; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
        }
        return dp[n];
    }
    int f2(vector<int>& nums) {
        int n = nums.size();
        int f0 = 0, f1 = 0, f2;
        for (int x : nums){
            f2 = max(f1, f0 + x);
            f0 = f1;
            f1 = f2;
        }
        return f1;
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        vector<int> nums1(nums.begin(), nums.end() - 1);
        vector<int> nums2(nums.begin() + 1, nums.end());
        return max(f1(nums1), f1(nums2));
        // return max(f2(nums1), f2(nums2));
    }
};
// @lc code=end


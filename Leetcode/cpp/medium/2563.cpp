/*
 * @lc app=leetcode.cn id=2563 lang=cpp
 *
 * [2563] 统计公平数对的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        long long ans = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; ++i) {
            ans += upper_bound(nums.begin(), nums.begin() + i, upper - nums[i]) - lower_bound(nums.begin(), nums.begin() + i, lower - nums[i]);
        }
        return ans;
    }
};
// @lc code=end


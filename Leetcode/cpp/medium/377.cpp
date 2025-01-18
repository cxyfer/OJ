/*
 * @lc app=leetcode.cn id=377 lang=cpp
 *
 * [377] 组合总和 Ⅳ
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;
        for (int cur = 1; cur <= target; ++cur) {
            for (int x : nums) {
                if (cur >= x) dp[cur] += dp[cur - x];
            }
        }
        return dp[target];
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int rob(vector<int>& nums) {
        // return solve1(nums);
        // return solve2(nums);
        return solve3(nums);
    }
    int solve1(vector<int>& nums) {
        int n = nums.size();
        vector<int> memo(n, -1);
        function<int(int)> dfs = [&](int i) -> int {
            if (i < 0) return 0;
            if (memo[i] != -1) return memo[i];
            return memo[i] = max(dfs(i - 1), dfs(i - 2) + nums[i]);
        };
        return dfs(n - 1);
    }
    int solve2(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n + 1, 0);
        dp[1] = nums[0];
        for (int i = 2; i <= n; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
        }
        return dp[n];
    }
    int solve3(vector<int>& nums) {
        int n = nums.size();
        int f0 = 0, f1 = 0, f2;
        for (int x : nums){
            f2 = max(f1, f0 + x);
            f0 = f1;
            f1 = f2;
        }
        return f1;
    }
};
// @lc code=end


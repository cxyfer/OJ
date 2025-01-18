/*
 * @lc app=leetcode.cn id=494 lang=cpp
 *
 * [494] 目标和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        target += accumulate(nums.begin(), nums.end(), 0);
        if (target % 2 || target < 0) return 0;
        target /= 2;
        vector<vector<int>> memo(n + 1, vector<int>(target + 1, -1));
        function<int(int, int)> dfs = [&](int i, int j) -> int {
            if (i == 0) return j == 0;
            if (memo[i][j] != -1) return memo[i][j];
            if (j < nums[i - 1]) return dfs(i - 1, j); // Pruning
            return memo[i][j] = dfs(i - 1, j) + dfs(i - 1, j - nums[i - 1]);
        };
        return dfs(n, target);
    }
};

class Solution2 {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        target += accumulate(nums.begin(), nums.end(), 0);
        if (target % 2 || target < 0) return 0;
        target /= 2;
        vector<int> dp(target + 1);
        dp[0] = 1;
        for (int i = 0; i < n; i++)
            for (int j = target; j >= nums[i]; j--)
                dp[j] += dp[j - nums[i]];
        return dp[target];
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};

// @lc code=end
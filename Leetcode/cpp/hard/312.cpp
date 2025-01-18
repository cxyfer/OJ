/*
 * @lc app=leetcode.cn id=312 lang=cpp
 *
 * [312] 戳气球
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr(n + 2, 1);
        for (int i = 1; i <= n; i++) arr[i] = nums[i - 1];
        vector<vector<int>> memo(n + 2, vector<int>(n + 2, -1));
        function<int(int, int)> dfs = [&](int left, int right) -> int {
            if (right - left <= 1) return 0;
            if (memo[left][right] != -1) return memo[left][right];
            int res = 0;
            for (int i = left + 1; i < right; i++) {
                int cur = arr[left] * arr[i] * arr[right];
                cur += dfs(left, i) + dfs(i, right);
                res = max(res, cur);
            }
            return memo[left][right] = res;
        };
        return dfs(0, n + 1);
    }
};

class Solution2 {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr(n + 2, 1);
        for (int i = 1; i <= n; i++) arr[i] = nums[i - 1];
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        for (int ln = 3; ln <= n + 2; ln++) {  // length of subarray
            for (int left = 0; left <= n + 2 - ln; left++) {
                int right = left + ln - 1;
                for (int i = left + 1; i < right; i++) {
                    int cur = dp[left][i] + dp[i][right] +
                              arr[left] * arr[i] * arr[right];
                    dp[left][right] = max(dp[left][right], cur);
                }
            }
        }
        return dp[0][n + 1];
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end
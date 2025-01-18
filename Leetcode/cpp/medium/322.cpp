/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end());
        vector<int> dp(amount+1, INT_MAX / 2);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int c : coins) {
                if (i < c) break;
                dp[i] = min(dp[i], dp[i-c] + 1);
            }
        }
        return dp[amount] == INT_MAX / 2 ? -1 : dp[amount];
    }
};
// @lc code=end


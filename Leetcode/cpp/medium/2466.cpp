/*
 * @lc app=leetcode.cn id=2466 lang=cpp
 *
 * [2466] 统计构造好字符串的方案数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<int> dp(high + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= high; ++i) {
            if (i >= zero) dp[i] += dp[i - zero];
            if (i >= one) dp[i] += dp[i - one];
            dp[i] %= MOD;
        }
        int ans = 0;
        for (int i = low; i <= high; ++i) {
            ans = (ans + dp[i]) % MOD;
        }
        return ans;
    }
};
// @lc code=end


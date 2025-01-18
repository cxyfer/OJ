/*
 * @lc app=leetcode id=1155 lang=cpp
 * @lcpr version=30112
 *
 * [1155] Number of Dice Rolls With Target Sum
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int MOD = 1e9 + 7;
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        vector<vector<LL>> dp(n + 1, vector<LL>(target + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; ++i) { // i個骰子
            for (int j = i; j <= target; ++j) { // 考慮前i個骰子，和為j的情況
                for (int x = 1; x <= k; ++x) { // 第i個骰子的點數
                    if (j-x < 0) break;
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % MOD;
                }
            }
        }
        return dp[n][target];
    }
};
// @lc code=end



/*
// @lcpr case=start
// 1\n6\n3\n
// @lcpr case=end

// @lcpr case=start
// 2\n6\n7\n
// @lcpr case=end

// @lcpr case=start
// 30\n30\n500\n
// @lcpr case=end

 */


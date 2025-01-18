/*
 * @lc app=leetcode.cn id=1449 lang=cpp
 *
 * [1449] 数位成本和为目标值的最大数字
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string largestNumber(vector<int>& cost, int target) {
        vector<int> dp(target + 1, -1);
        dp[0] = 0;
        for (int i = 1; i <= target; i++) {
            for (int j = 0; j < cost.size(); j++) {
                if (i >= cost[j] && dp[i - cost[j]] != -1) {
                    dp[i] = max(dp[i], dp[i - cost[j]] + 1);
                }
            }
        }
        if (dp[target] == -1) {
            return "0";
        }
        string ans = "";
        for (int i = 9; i >= 1; i--) {
            while (target >= cost[i - 1] && dp[target - cost[i - 1]] == dp[target] - 1) {
                ans += to_string(i);
                target -= cost[i - 1];
            }
        }
        return ans;
    }
};
// @lc code=end


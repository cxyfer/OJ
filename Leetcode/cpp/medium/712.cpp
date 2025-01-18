/*
 * @lc app=leetcode.cn id=712 lang=cpp
 *
 * [712] 两个字符串的最小ASCII删除和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minimumDeleteSum(string s, string t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));
        int s_sum = accumulate(s.begin(), s.end(), 0);
        int t_sum = accumulate(t.begin(), t.end(), 0);

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + s[i - 1];  
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return s_sum + t_sum - 2 * dp[m][n];
    }
};

class Solution2 {
public:
    int minimumDeleteSum(string s, string t) {
        int m = s.size(), n = t.size();
        // dp[i][j] 表示 s[:i] 和 t[:j] 相同所需的最小 ASCII 刪除和
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));
        for (int i = 1; i <= m; ++i) {
            dp[i][0] = dp[i - 1][0] + s[i - 1];
        }
        for (int j = 1; j <= n; ++j) {
            dp[0][j] = dp[0][j - 1] + t[j - 1];
        }
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == t[j - 1]) { // 相同，不用刪除
                    dp[i][j] = dp[i - 1][j - 1];
                } else { // 不同，刪除兩者之一，取最小
                    dp[i][j] = min(dp[i - 1][j] + s[i - 1], dp[i][j - 1] + t[j - 1]);
                }
            }
        }
        return dp[m][n];
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end


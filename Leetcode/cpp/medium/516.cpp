/*
 * @lc app=leetcode.cn id=516 lang=cpp
 *
 * [516] 最长回文子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    1. 轉換為 LCS 問題
    2. 區間 DP (Top-Down)
    3. 區間 DP (Bottom-Up)
        - 寫法一：枚舉長度，由小區間到大區間
        - 寫法二：一比一翻譯，i 要由大到小，j 要由小到大
*/
class Solution1 {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        string t = s;
        reverse(t.begin(), t.end());
        vector<vector<int>> dp(n + 1, vector<int>(n + 1));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[n][n];
    }
};

class Solution2 {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> memo(n, vector<int>(n, -1));
        auto f = [&](auto &&f, int i, int j) -> int {
            if (i > j) return 0;
            if (i == j) return 1;
            int& res = memo[i][j];
            if (res != -1) return res;
            if (s[i] == s[j]) return res = f(f, i + 1, j - 1) + 2;
            return res = max(f(f, i + 1, j), f(f, i, j - 1));
        };
        return f(f, 0, n - 1);
    }
};

class Solution3a {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> f(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) f[i][i] = 1;
        for (int ln = 2; ln <= n; ++ln) {
            for (int i = 0; i <= n - ln; ++i) {
                int j = i + ln - 1;
                if (s[i] == s[j]) f[i][j] = f[i + 1][j - 1] + 2;
                else f[i][j] = max(f[i + 1][j], f[i][j - 1]);
            }
        }
        return f[0][n - 1];
    }
};

class Solution3b {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> f(n, vector<int>(n, 0));
        for (int i = n - 1; i >= 0; i--) {
            f[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) f[i][j] = f[i + 1][j - 1] + 2;
                else f[i][j] = max(f[i + 1][j], f[i][j - 1]);
            }
        }
        return f[0][n - 1];
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// class Solution : public Solution3a {};
class Solution : public Solution3b {};
// @lc code=end
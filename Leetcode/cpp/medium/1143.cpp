/*
 * @lc app=leetcode.cn id=1143 lang=cpp
 *
 * [1143] 最长公共子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int longestCommonSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> memo(m, vector<int>(n, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            if (i < 0 || j < 0) return 0;
            int& res = memo[i][j];
            if (res != -1) return res;
            if (s[i] == t[j]) return res = dfs(i - 1, j - 1) + 1;
            return res = max(dfs(i - 1, j), dfs(i, j - 1));
        };
        return dfs(m - 1, n - 1);
    }
};

class Solution2 {
public:
    int longestCommonSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> f(m + 1, vector<int>(n + 1));
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                if (s[i - 1] == t[j - 1])
                    f[i][j] = f[i - 1][j - 1] + 1;
                else
                    f[i][j] = max(f[i - 1][j], f[i][j - 1]);
        return f[m][n];
    }
};

class Solution3 {
public:
    int longestCommonSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        s = " " + s + " ";
        t = " " + t + " ";
        vector<vector<int>> f(m + 2, vector<int>(n + 2));
        auto checkmax = [&](int& a, int b) {
            if (b > a) a = b;
        };
        for (int i = 0; i <= m; ++i)
            for (int j = 0; j <= n; ++j) {
                checkmax(f[i + 1][j], f[i][j]);
                checkmax(f[i][j + 1], f[i][j]);
                checkmax(f[i + 1][j + 1], f[i][j] + (s[i + 1] == t[j + 1]));
            }
        return f[m][n];
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
using Solution = Solution3;
// @lc code=end


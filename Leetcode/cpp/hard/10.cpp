/*
 * @lc app=leetcode.cn id=10 lang=cpp
 * @lcpr version=30204
 *
 * [10] 正则表达式匹配
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        vector<vector<int>> memo(n, vector<int>(m, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> bool {
            if (i < 0) return j < 0 || (p[j] == '*' && dfs(i, j - 2));
            if (j < 0) return false;
            int& res = memo[i][j];
            if (res != -1) return res;
            if (p[j] == '*') return res = dfs(i, j - 2) || ((s[i] == p[j - 1] || p[j - 1] == '.') && dfs(i - 1, j));
            if (s[i] == p[j] || p[j] == '.') return res = dfs(i - 1, j - 1);
            return res = false;
        };
        return dfs(n - 1, m - 1);
    }
};

class Solution2 {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        s = " " + s;
        p = " " + p;
        vector<vector<bool>> f(n + 1, vector<bool>(m + 1, false));
        f[0][0] = true;
        for (int j = 2; j <= m; ++j) f[0][j] = f[0][j - 2] && p[j] == '*';
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                if (p[j] == '*')
                    f[i][j] = f[i][j - 2] || ((s[i] == p[j - 1] || p[j - 1] == '.') && f[i - 1][j]);
                else if (p[j] == '.' || s[i] == p[j])
                    f[i][j] = f[i - 1][j - 1];
        return f[n][m];
    }
};

class Solution3 {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        s = " " + s + " ";
        p = " " + p + " ";
        vector<vector<int>> f(n + 2, vector<int>(m + 3, 0));
        f[0][0] = 1;
        for (int i = 0; i <= n; ++i)
            for (int j = 0; j <= m; ++j) {
                if (p[j + 2] == '*') {
                    f[i][j + 2] |= f[i][j];
                    if (s[i + 1] == p[j + 1] || p[j + 1] == '.')
                        f[i + 1][j] |= f[i][j];
                }
                if (s[i + 1] == p[j + 1] || p[j + 1] == '.')
                    f[i + 1][j + 1] |= f[i][j];
            }
        return f[n][m];
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// using Solution = Solution3;
// @lc code=end

/*
// @lcpr case=start
// "aa"\n"a"\n
// @lcpr case=end

// @lcpr case=start
// "aa"\n"a*"\n
// @lcpr case=end

// @lcpr case=start
// "ab"\n".*"\n
// @lcpr case=end

 */


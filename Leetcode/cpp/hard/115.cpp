/*
 * @lc app=leetcode.cn id=115 lang=cpp
 * @lcpr version=30204
 *
 * [115] 不同的子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using ull = unsigned long long;

class Solution1 {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<vector<int>> memo(n, vector<int>(m, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            if (n - i < m - j) return 0;
            if (j == m) return 1;
            int& res = memo[i][j];
            if (res != -1) return res;
            return res = dfs(i + 1, j) + (s[i] == t[j] ? dfs(i + 1, j + 1) : 0);
        };
        return dfs(0, 0);
    }
};

class Solution2a {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<vector<int>> memo(n, vector<int>(m, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            if (i < j) return 0;
            if (j < 0) return 1;
            int& res = memo[i][j];
            if (res != -1) return res;
            return res = dfs(i - 1, j) + (s[i] == t[j] ? dfs(i - 1, j - 1) : 0);
        };
        return dfs(n - 1, m - 1);
    }
};

class Solution2b {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        // 有些和答案無關的轉移可能會導致溢出，所以用 unsigned long long
        vector<vector<ull>> f(n + 1, vector<ull>(m + 1, 0));
        for (int i = 0; i <= n; ++i) f[i][0] = 1;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                f[i][j] = f[i - 1][j] + (s[i - 1] == t[j - 1] ? f[i - 1][j - 1] : 0);
        return f[n][m];
    }
};

class Solution2c {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        // 有些和答案無關的轉移可能會導致溢出，所以用 unsigned long long
        vector<vector<ull>> f(2, vector<ull>(m + 1, 0));
        f[0][0] = f[1][0] = 1;
        for (int i = 1; i <= n; ++i) {
            int cur = i & 1, pre = (i - 1) & 1;
            for (int j = 1; j <= m; ++j)
                f[cur][j] = f[pre][j] + (s[i - 1] == t[j - 1] ? f[pre][j - 1] : 0);
        }
        return f[n & 1][m];
    }
};

class Solution2d {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<ull> f(m + 1, 0);
        f[0] = 1;
        for (int i = 1; i <= n; ++i)
            for (int j = m; j >= 1; --j)
                if (s[i - 1] == t[j - 1])
                    f[j] += f[j - 1];
        return f[m];
    }
};

// using Solution = Solution1;
using Solution = Solution2a;
// using Solution = Solution2b;
// using Solution = Solution2c;
// using Solution = Solution2d;
// @lc code=end



/*
// @lcpr case=start
// "rabbbit"\n"rabbit"\n
// @lcpr case=end

// @lcpr case=start
// "babgbag"\n"bag"\n
// @lcpr case=end

 */


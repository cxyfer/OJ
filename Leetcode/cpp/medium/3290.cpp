/*
 * @lc app=leetcode.cn id=3290 lang=cpp
 * @lcpr version=30204
 *
 * [3290] 最高乘法得分
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using ll = long long;

class Solution1 {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        int n = a.size(), m = b.size();
        vector<vector<ll>> memo(n, vector<ll>(m, LLONG_MIN));
        auto dfs = [&](this auto&& dfs, int i, int j) -> ll {
            if (i == n) return 0;
            if (j == m) return LLONG_MIN / 2;
            ll& res = memo[i][j];
            if (res != LLONG_MIN) return res;
            return res = max(dfs(i, j + 1),
                             dfs(i + 1, j + 1) + 1LL * a[i] * b[j]);
        };
        return dfs(0, 0);
    }
};

class Solution2a {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        int n = a.size(), m = b.size();
        vector<vector<ll>> memo(n, vector<ll>(m, LLONG_MIN));
        auto dfs = [&](this auto&& dfs, int i, int j) -> ll {
            if (i < 0) return 0;
            if (j < 0) return LLONG_MIN / 2;
            ll& res = memo[i][j];
            if (res != LLONG_MIN) return res;
            return res = max(dfs(i, j - 1),
                             dfs(i - 1, j - 1) + 1LL * a[i] * b[j]);
        };
        return dfs(n - 1, m - 1);
    }
};

class Solution2b {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        int n = a.size(), m = b.size();
        vector<vector<ll>> f(n + 1, vector<ll>(m + 1, 0));
        for (int i = 1; i <= n; ++i) f[i][0] = LLONG_MIN / 2;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                f[i][j] = max(f[i][j - 1],
                              f[i - 1][j - 1] + 1LL * a[i - 1] * b[j - 1]);
        return f[n][m];
    }
};

class Solution2c {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        int n = a.size(), m = b.size();
        vector<vector<ll>> f(2, vector<ll>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            int cur = i & 1, pre = (i - 1) & 1;
            f[cur][0] = LLONG_MIN / 2;
            for (int j = 1; j <= m; ++j)
                f[cur][j] = max(f[cur][j - 1],
                                f[pre][j - 1] + 1LL * a[i - 1] * b[j - 1]);
        }
        return f[n & 1][m];
    }
};

// using Solution = Solution1;
// using Solution = Solution2a;
// using Solution = Solution2b;
using Solution = Solution2c;
// @lc code=end



/*
// @lcpr case=start
// [3,2,5,6]\n[2,-6,4,-5,-3,2,-7]\n
// @lcpr case=end

// @lcpr case=start
// [-1,4,5,-2]\n[-5,-1,-3,-2,-4]\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=62 lang=cpp
 * @lcpr version=30204
 *
 * [62] 不同路径
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int MAX_N = 201;
const int MAX_V = 2e9 + 5;
vector<vector<LL>> comb(MAX_N, vector<LL>(MAX_N, 1));

auto init = []() {
    for (int i = 1; i < MAX_N; i++)
        for (int j = 1; j < i; j++) {
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            if (comb[i][j] > MAX_V) comb[i][j] = MAX_V;
        }
    return 0;
}();

class Solution1 {
public:
    int uniquePaths(int m, int n) {
        return comb[m + n - 2][m - 1];
    }
};

class Solution2 {
public:
    int uniquePaths(int m, int n) {
        // 令 f(i, j) 為從 (i, j) 到 (m-1, n-1) 的路徑數
        vector<vector<int>> memo(m, vector<int>(n, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            if (i == m - 1 && j == n - 1) return 1;
            if (i >= m || j >= n) return 0;
            if (memo[i][j] != -1) return memo[i][j];
            return memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1);
        };
        return dfs(0, 0);
    }
};

class Solution3a {
public:
    int uniquePaths(int m, int n) {
        // 令 f(i, j) 為從 (0, 0) 到 (i, j) 的路徑數
        vector<vector<int>> memo(m, vector<int>(n, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            if (i == 0 && j == 0) return 1;
            if (i < 0 || j < 0) return 0;
            if (memo[i][j] != -1) return memo[i][j];
            return memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1);
        };
        return dfs(m - 1, n - 1);
    }
};

class Solution3b {
public:
    int uniquePaths(int m, int n) {
        // 令 f(i, j) 為從 (0, 0) 到 (i, j) 的路徑數
        vector<vector<int>> f(m + 1, vector<int>(n + 1, 0));
        f[1][1] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (i == 1 && j == 1) continue;
                f[i][j] = f[i - 1][j] + f[i][j - 1];
            }
        return f[m][n];
    }
};

class Solution3c {
public:
    int uniquePaths(int m, int n) {
        vector<int> f(n + 1, 0), nf(n + 1, 0);
        f[1] = 1;
        for (int i = 1; i <= m; ++i) {
            fill(nf.begin(), nf.end(), 0);
            for (int j = 1; j <= n; ++j)
                nf[j] = nf[j - 1] + f[j];
            swap(f, nf);
        }
        return f[n];
    }
};

class Solution3d {
public:
    int uniquePaths(int m, int n) {
        vector<int> f(n + 1, 0);
        f[1] = 1;
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                f[j] = f[j - 1] + f[j];
        return f[n];
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
// using Solution = Solution3a;
// using Solution = Solution3b;
// using Solution = Solution3c;
using Solution = Solution3d;
// @lc code=end



/*
// @lcpr case=start
// 3\n7\n
// @lcpr case=end

// @lcpr case=start
// 3\n2\n
// @lcpr case=end

// @lcpr case=start
// 7\n3\n
// @lcpr case=end

// @lcpr case=start
// 3\n3\n
// @lcpr case=end

 */


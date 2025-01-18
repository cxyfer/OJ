/*
 * @lc app=leetcode.cn id=1277 lang=cpp
 *
 * [1277] 统计全为 1 的正方形子矩阵
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> memo(m, vector<int>(n, -1));
        auto dfs = [&](auto&& dfs, int i, int j) -> int {
            if (i < 0 || j < 0) return 0;
            int& res = memo[i][j];
            if (res != -1) return res;
            if (matrix[i][j] == 0) return res = 0;
            return res = 1 + min({dfs(dfs, i - 1, j), dfs(dfs, i, j - 1), dfs(dfs, i - 1, j - 1)});
        };
        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                ans += dfs(dfs, i, j);
        return ans;
    }
};

class Solution2 {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> f(m, vector<int>(n));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) continue;
                if (i == 0 || j == 0) {
                    f[i][j] = 1;
                } else {
                    f[i][j] = min({f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]}) + 1;
                }
            }
        }
        int ans = 0;
        for (const auto& row : f)
            ans += accumulate(row.begin(), row.end(), 0);
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end


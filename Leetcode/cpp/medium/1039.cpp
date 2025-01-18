/*
 * @lc app=leetcode.cn id=1039 lang=cpp
 *
 * [1039] 多边形三角剖分的最低得分
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minScoreTriangulation(vector<int>& v) {
        int n = v.size();
        vector<vector<int>> memo(n, vector<int>(n, -1));
        auto f = [&](auto &&f, int i, int j) -> int {
            if (i + 1 >= j) return 0;
            int &res = memo[i][j];
            if (res != -1) return res;
            res = INT_MAX;
            for (int k = i + 1; k < j; ++k) {
                res = min(res, f(f, i, k) + f(f, k, j) + v[i] * v[k] * v[j]);
            }
            return res;
        };
        return f(f, 0, n - 1);
    }
};

class Solution2a {
public:
    int minScoreTriangulation(vector<int>& v) {
        int n = v.size();
        vector<vector<int>> f(n, vector<int>(n, 0));
        for (int ln = 3; ln <= n; ++ln) { // 枚舉長度
            for (int i = 0; i <= n - ln; ++i) { // 枚舉左端點
                int j = i + ln - 1; // 右端點
                f[i][j] = INT_MAX;
                for (int k = i + 1; k < j; ++k) { // 枚舉分界點
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + v[i] * v[k] * v[j]);
                }
            }
        }
        return f[0][n - 1];
    }
};

class Solution2b {
public:
    int minScoreTriangulation(vector<int>& v) {
        int n = v.size();
        vector<vector<int>> f(n, vector<int>(n, 0));
        for (int i = n - 3; i >= 0; --i) {
            for (int j = i + 2; j < n; ++j) {
                f[i][j] = INT_MAX;
                for (int k = i + 1; k < j; ++k) {
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + v[i] * v[k] * v[j]);
                }
            }
        }
        return f[0][n - 1];
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2a {};
class Solution : public Solution2b {};
// @lc code=end
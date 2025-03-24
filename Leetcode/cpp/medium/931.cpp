/*
 * @lc app=leetcode.cn id=931 lang=cpp
 * @lcpr version=30204
 *
 * [931] 下降路径最小和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>> memo(n, vector<int>(n, INT_MAX / 2));
        auto f = [&](auto&& f, int i, int j) -> int {
            if (i == n) return 0;
            if (j < 0 or j >= n) return INT_MAX / 2;
            int& res = memo[i][j];
            if (res != INT_MAX / 2) return res;
            return res = matrix[i][j] + min({f(f, i + 1, j - 1), f(f, i + 1, j), f(f, i + 1, j + 1)});
        };
        int ans = INT_MAX / 2;
        for (int j = 0; j < n; j++)
            ans = min(ans, f(f, 0, j));
        return ans;
    }
};

class Solution2a {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // f[i][j] 表示從 (i, j - 1) 開始的最小下降路徑和
        vector<vector<int>> f(n, vector<int>(n + 2, INT_MAX / 2));
        for (int j = 0; j < n; j++) f[n - 1][j + 1] = matrix[n - 1][j];
        for (int i = n - 2; i >= 0; i--)
            for (int j = 1; j <= n; j++)
                f[i][j] = matrix[i][j - 1] + min({f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1]});
        return *min_element(f[0].begin() + 1, f[0].end() - 1);
    }
};

class Solution2b {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> f(n + 2, INT_MAX / 2), nf(n + 2, INT_MAX / 2);
        for (int j = 0; j < n; j++) f[j + 1] = matrix[n - 1][j];
        for (int i = n - 2; i >= 0; i--) {
            fill(nf.begin(), nf.end(), INT_MAX / 2);
            for (int j = 1; j <= n; j++)
                nf[j] = matrix[i][j - 1] + min({f[j - 1], f[j], f[j + 1]});
            swap(f, nf);
        }
        return *min_element(f.begin() + 1, f.end() - 1);
    }
};

class Solution2c {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> f(n + 2, INT_MAX / 2), nf(n + 2, INT_MAX / 2);
        for (int j = 0; j < n; j++) f[j + 1] = matrix[n - 1][j];
        for (int i = n - 2; i >= 0; i--) {
            int pre = f[0];
            for (int j = 1; j <= n; j++) {
                int t = f[j];
                f[j] = matrix[i][j - 1] + min({pre, f[j], f[j + 1]});
                pre = t;
            }
        }
        return *min_element(f.begin() + 1, f.end() - 1);
    }
};

// using Solution = Solution1;
// using Solution = Solution2a;
// using Solution = Solution2b;
using Solution = Solution2c;
// @lc code=end



/*
// @lcpr case=start
// [[2,1,3],[6,5,4],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[-19,57],[-40,-5]]\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=120 lang=cpp
 * @lcpr version=30204
 *
 * [120] 三角形最小路径和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> memo(n, vector<int>(n, INT_MIN / 2));
        auto f = [&](auto&& f, int i, int j) -> int {
            if (i == n) return 0;
            int& res = memo[i][j];
            if (res != INT_MIN / 2) return res;
            return res = triangle[i][j] + min(f(f, i + 1, j), f(f, i + 1, j + 1));
        };
        return f(f, 0, 0);
    }
};

class Solution2a {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> f(n, vector<int>(n, 0));
        f[n - 1] = triangle[n - 1];
        for (int i = n - 2; i >= 0; i--)
            for (int j = 0; j <= i; j++)
                f[i][j] = triangle[i][j] + min(f[i + 1][j], f[i + 1][j + 1]);
        return f[0][0];
    }
};

class Solution2b {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> f(n, 0), nf(n, 0);
        f = triangle[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            fill(nf.begin(), nf.end(), 0);
            for (int j = 0; j <= i; j++)
                nf[j] = triangle[i][j] + min(f[j], f[j + 1]);
            swap(f, nf);
        }
        return f[0];
    }
};

class Solution2c {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> f(n, 0);
        f = triangle[n - 1];
        for (int i = n - 2; i >= 0; i--)
            for (int j = 0; j <= i; j++)
                f[j] = triangle[i][j] + min(f[j], f[j + 1]);
        return f[0];
    }
};

// using Solution = Solution1;
// using Solution = Solution2a;
// using Solution = Solution2b;
using Solution = Solution2c;
// @lc code=end



/*
// @lcpr case=start
// [[2],[3,4],[6,5,7],[4,1,8,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[-10]]\n
// @lcpr case=end

 */


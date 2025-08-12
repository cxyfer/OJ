/*
 * @lc app=leetcode.cn id=2787 lang=cpp
 * @lcpr version=30204
 *
 * [2787] 将一个数字表示成幂的和的方案数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
const int MAX_N = 300;
const int MAX_X = 5;
vector<vector<int>> f(MAX_X + 1, vector<int>(MAX_N + 1, 0));
auto init = []() {
    for (int x = 0; x <= MAX_X; ++x)
        f[x][0] = 1;
    for (int x = 1; x <= MAX_X; ++x) {
        for (int i = 1; i <= MAX_N; ++i) {
            int v = pow(i, x);
            if (v > MAX_N) break;
            for (int s = MAX_N; s >= v; --s)
                f[x][s] = (f[x][s] + f[x][s - v]) % MOD;
        }
    }
    return 0;
}();

class Solution {
public:
    int numberOfWays(int n, int x) {
        return f[x][n];
    }
};
// @lc code=end



/*
// @lcpr case=start
// 10\n2\n
// @lcpr case=end

// @lcpr case=start
// 4\n1\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=279 lang=cpp
 *
 * [279] 完全平方数
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 1e4;
vector<int> f(N + 1, INT_MAX);
auto init = []() {
    f[0] = 0;
    for (int i = 1; i * i <= N; i++)
        for (int j = i * i; j <= N; j++) f[j] = min(f[j], f[j - i * i] + 1);
    return 0;
}();

class Solution {
public:
    int numSquares(int n) {
        return f[n];
    }
};
// @lc code=end

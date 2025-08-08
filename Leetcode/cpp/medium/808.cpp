/*
 * @lc app=leetcode.cn id=808 lang=cpp
 * @lcpr version=30204
 *
 * [808] 分汤
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAX_M = (5000 + 24) / 25;
vector<vector<double>> memo(MAX_M + 1, vector<double>(MAX_M + 1, -1));
double dfs(int a, int b) {
    if (a <= 0 && b <= 0) return 0.5;
    if (a <= 0) return 1.0;
    if (b <= 0) return 0.0;
    if (memo[a][b] != -1) return memo[a][b];
    return memo[a][b] = 0.25 * (dfs(a - 4, b) + dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3));
}

auto init = []() {
    dfs(MAX_M, MAX_M);
    return 0;
}();

class Solution {
public:
    double soupServings(int n) {
        int m = (n + 24) / 25;
        if (m > MAX_M) return 1.0;
        return dfs(m, m);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 50\n
// @lcpr case=end

// @lcpr case=start
// 100\n
// @lcpr case=end

 */


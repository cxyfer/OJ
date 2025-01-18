/*
 * @lc app=leetcode.cn id=526 lang=cpp
 *
 * [526] 优美的排列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countArrangement(int n) {
        int u = (1 << n) - 1;
        vector<int> memo = vector<int>(1 << n, -1);

        function<int(int)> dfs = [&](int s) -> int {
            if (s == u) return 1;
            if (memo[s] != -1) return memo[s];
            int res = 0;
            int i = __builtin_popcount(s) + 1;
            for (int j = 1; j <= n; j++) {
                if ((s >> (j - 1)) & 1) continue;
                if (i % j == 0 || j % i == 0) {
                    res += dfs(s | (1 << (j - 1)));
                }
            }
            return memo[s] = res;
        };
        return dfs(0);
    }
};
// @lc code=end
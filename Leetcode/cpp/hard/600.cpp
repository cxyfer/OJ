/*
 * @lc app=leetcode.cn id=600 lang=cpp
 *
 * [600] 不含连续1的非负整数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findIntegers(int n) {
        int m = __lg(n);
        int memo[m + 1][2][2];
        memset(memo, -1, sizeof(memo));
        function<int(int, bool, bool)> dfs = [&](int i, bool pre, bool is_limit) {
            if (i < 0) return 1; // 填完所有位數
            if (memo[i][pre][is_limit] != -1) return memo[i][pre][is_limit];
            int up = is_limit ? (n >> i) & 1 : 1; // 當前可以填的數字上界
            int res = dfs(i - 1, false, is_limit && up == 0); // 當前位數填0
            if (!pre && up == 1) { // 若前一位是0，且當前位可以填入1
                res += dfs(i - 1, true, is_limit); // 當前位數填1
            }
            return memo[i][pre][is_limit] = res;
        };
        return dfs(m, false, true);
    }
};
// @lc code=end
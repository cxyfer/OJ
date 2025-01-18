/*
 * @lc app=leetcode.cn id=3154 lang=cpp
 *
 * [3154] Find Number of Ways to Reach the K-th Stair
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int waysToReachStair(int k) {
        unordered_map<int, int> memo[32][2];
        function<int(int, int, bool)> f = [&](int x, int j, bool flag) -> int {
            if (x < 0) return 0;
            if (x > k + 1) return 0;
            if (memo[j][flag].count(x)) return memo[j][flag][x];
            int res = (x == k) ? 1 : 0;
            if (flag) res += f(x - 1, j, false);
            res += f(x + (1 << j), j + 1, true);
            return memo[j][flag][x] = res;
        };
        return f(1, 0, true);
    }
};
// @lc code=end


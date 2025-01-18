/*
 * @lc app=leetcode.cn id=1553 lang=cpp
 *
 * [1553] 吃掉 N 个橘子的最少天数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        DP，考慮三種情況：
        1. 今天吃 1 個，明天吃 n-1 個
        2. 若 n % 2 == 0，今天吃 n//2 個，明天吃 n//2 個
        3. 若 n % 3 == 0，今天吃 2n//3 個，明天吃 n//3 個
        Time complexity: O(n)

        但由於 n 的範圍很大， O(n) 的時間複雜度會超時，因此可以去除第一種情況，只考慮後兩種情況：
        1. 若 n % 2 == 1，則今天吃 1 個，明天就可以吃 n//2 個，剩下 n//2 個遞迴
            即需要吃 n % 2 + 1 + dfs(n // 2) 天
        2. 若 n % 3 == 1, 2 ，則連續 1/2 天吃 1 個，再來吃 2n//3 個，剩下 n//3 個遞迴
            即需要吃 n % 3 + 1 + dfs(n // 3) 天
        Time complexity: O(log n)
    */
    unordered_map<int, int> dp;
    int minDays(int n) {
        if (n <= 1) return n;
        if (dp.count(n)) return dp[n];
        return dp[n] = 1 + min(n % 2 + minDays(n / 2), n % 3 + minDays(n / 3));
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=2207 lang=cpp
 *
 * [2207] 字符串中最多数目的子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maximumSubsequenceCount(string text, string pattern) {
        int n = text.size(), x = pattern[0], y = pattern[1];
        long long ans = 0, cnt_x = 0, cnt_y = 0;
        for (char ch : text) {
            // 先處理 y 是因為可能有 x == y 的情況，因此也不能用 else if
            if (ch == y) {
                ans += cnt_x;
                cnt_y++;
            }
            if (ch == x) {
                cnt_x++; // prefix sum
            }
        }
        // 最後加上添加一個字元的最大收益，即 max(cnt_x, cnt_y)
        return ans + max(cnt_x, cnt_y); 
    }
};
// @lc code=end


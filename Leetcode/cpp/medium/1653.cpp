/*
 * @lc app=leetcode.cn id=1653 lang=cpp
 *
 * [1653] 使字符串平衡的最少删除次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.size(), a = 0, b = 0;
        for (char ch : s) {
            if (ch == 'a') a++;
            else b = max(a, b) + 1;
        }
        return n - max(a, b);
    }
};
// @lc code=end


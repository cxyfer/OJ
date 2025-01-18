/*
 * @lc app=leetcode.cn id=2414 lang=cpp
 *
 * [2414] 最长的字母序连续子字符串的长度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int longestContinuousSubstring(string s) {
        int n = s.size();
        int ans = 1, cur = 1;
        for (int i = 1; i < n; i++) {
            if (s[i] - s[i - 1] == 1) ans = max(ans, ++cur);
            else cur = 1;
        }
        return ans;
    }
};
// @lc code=end


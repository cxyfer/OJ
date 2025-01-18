/*
 * @lc app=leetcode.cn id=2486 lang=cpp
 *
 * [2486] 追加字符以获得子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int appendCharacters(string s, string t) {
        int n = s.size(), m = t.size();
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (s[i] == t[j]) j++;
            i++;
        }
        return m - j;
    }
};
// @lc code=end


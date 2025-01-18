/*
 * @lc app=leetcode.cn id=2734 lang=cpp
 *
 * [2734] 执行子串操作后的字典序最小字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string smallestString(string s) {
        int n = s.size();
        bool flag = false;
        for (int i = 0; i < n; i++) {
            if (flag && s[i] == 'a') break;
            if (s[i] != 'a'){
                flag = true;
                s[i]--;
            }
        }
        if (!flag) s.back() = 'z';
        return s;
    }
};
// @lc code=end
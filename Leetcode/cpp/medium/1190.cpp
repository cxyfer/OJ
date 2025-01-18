/*
 * @lc app=leetcode.cn id=1190 lang=cpp
 *
 * [1190] 反转每对括号间的子串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string reverseParentheses(string s) {
        string st = "";
        for (char ch : s) {
            if (ch == ')') {
                string t = "";
                while (!st.empty() && st.back() != '(') {
                    t += st.back();
                    st.pop_back();
                }
                st.pop_back();
                st += t;
            } else {
                st.push_back(ch);
            }
        }
        return st;
    }
};
// @lc code=end
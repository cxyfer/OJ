/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Stack
    */
    bool isValid(string s) {
        stack<char> st;
        for (char ch : s){
            if (ch == '(') st.push(')');
            else if (ch == '[') st.push(']');
            else if (ch == '{') st.push('}');
            else {
                if (st.empty() || ch != st.top()) return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
// @lc code=end


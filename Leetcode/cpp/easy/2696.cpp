/*
 * @lc app=leetcode.cn id=2696 lang=cpp
 *
 * [2696] 删除子串后的字符串最小长度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minLength(string s) {
        stack<char> st;
        for (char ch : s) {
            if (st.size() && (st.top() == 'A' && ch == 'B' ||
                              st.top() == 'C' && ch == 'D')) {
                st.pop();
            } else {
                st.push(ch);
            }
        }
        return st.size();
    }
};
// @lc code=end


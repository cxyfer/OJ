/*
 * @lc app=leetcode.cn id=1047 lang=cpp
 * @lcpr version=30204
 *
 * [1047] Remove All Adjacent Duplicates In String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string removeDuplicates(string s) {
        string st;
        for (char ch : s) {
            if (!st.empty() && st.back() == ch) st.pop_back();
            else st.push_back(ch);
        }
        return st;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abbaca"\n
// @lcpr case=end

 */


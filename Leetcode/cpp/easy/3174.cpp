/*
 * @lc app=leetcode id=3174 lang=cpp
 *
 * [3174] Clear Digits
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string clearDigits(string s) {
        string st;
        for (auto ch : s) {
            if (isdigit(ch)) st.pop_back();
            else st.push_back(ch);
        }
        return st;
    }
};
// @lc code=end


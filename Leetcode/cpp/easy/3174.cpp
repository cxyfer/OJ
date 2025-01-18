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
        string ans = "";
        for (char ch : s) {
            if (isdigit(ch)) ans.pop_back();
            else ans += ch;
        }
        return ans;
    }
};
// @lc code=end


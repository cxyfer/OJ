/*
 * @lc app=leetcode.cn id=3324 lang=cpp
 *
 * [3324] 出现在屏幕上的字符串序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> stringSequence(string target) {
        vector<string> ans;
        string s;
        for (char ch : target) {
            s += 'a';
            ans.push_back(s);
            for (int i = 0; i < ch - 'a'; i++) {
                s.back() = s.back() + 1;
                ans.push_back(s);
            }
        }
        return ans;
    }
};
// @lc code=end


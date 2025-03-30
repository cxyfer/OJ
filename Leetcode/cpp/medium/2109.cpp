/*
 * @lc app=leetcode.cn id=2109 lang=cpp
 * @lcpr version=30204
 *
 * [2109] 向字符串添加空格
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string ans;
        int last = 0;
        for (int x : spaces) {
            ans += s.substr(last, x - last) + " ";
            last = x;
        }
        ans += s.substr(last);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "LeetcodeHelpsMeLearn"\n[8,13,15]\n
// @lcpr case=end

// @lcpr case=start
// "icodeinpython"\n[1,5,7,9]\n
// @lcpr case=end

// @lcpr case=start
// "spacing"\n[0,1,2,3,4,5,6]\n
// @lcpr case=end

 */


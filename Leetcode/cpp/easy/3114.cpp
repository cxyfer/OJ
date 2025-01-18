/*
 * @lc app=leetcode id=3114 lang=cpp
 * @lcpr version=30122
 *
 * [3114] Latest Time You Can Obtain After Replacing Characters
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string findLatestTime(string s) {
        if (s[0] == '?') s[0] = (s[1] == '?' || s[1] <= '1') ? '1' : '0';
        if (s[1] == '?') s[1] = (s[0] == '1') ? '1' : '9';
        if (s[3] == '?')  s[3] = '5';
        if (s[4] == '?') s[4] = '9';
        return s;
    }
};
// @lc code=end

/*
// @lcpr case=start
// "1?:?4"\n
// @lcpr case=end

// @lcpr case=start
// "0?:5?"\n
// @lcpr case=end

 */


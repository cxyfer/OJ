/*
 * @lc app=leetcode.cn id=2546 lang=cpp
 * @lcpr version=30204
 *
 * [2546] 执行逐位运算使字符串相等
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool makeStringsEqual(string s, string target) {
        return (s.find('1') != string::npos) == (target.find('1') != string::npos);
    }
};
// @lc code=end



/*
// @lcpr case=start
// "1010"\n"0110"\n
// @lcpr case=end

// @lcpr case=start
// "11"\n"00"\n
// @lcpr case=end

 */


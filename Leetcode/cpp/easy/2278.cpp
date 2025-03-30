/*
 * @lc app=leetcode.cn id=2278 lang=cpp
 * @lcpr version=30204
 *
 * [2278] 字母在字符串中的百分比
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int percentageLetter(string s, char letter) {
        return ranges::count(s, letter) * 100 / s.size();
    }
};
// @lc code=end



/*
// @lcpr case=start
// "foobar"\n"o"\n
// @lcpr case=end

// @lcpr case=start
// "jjjj"\n"k"\n
// @lcpr case=end

 */


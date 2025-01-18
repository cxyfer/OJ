/*
 * @lc app=leetcode.cn id=2710 lang=cpp
 *
 * [2710] 移除字符串中的尾随零
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string removeTrailingZeros(string num) {
        while (num.back() == '0') num.pop_back();
        return num;
    }
};
// @lc code=end


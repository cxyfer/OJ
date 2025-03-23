/*
 * @lc app=leetcode.cn id=3099 lang=cpp
 *
 * [3099] 哈沙德数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int s = 0, t = x;
        while (t) {
            s += t % 10;
            t /= 10;
        }
        return x % s == 0 ? s : -1;
    }
};
// @lc code=end


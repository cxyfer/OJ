/*
 * @lc app=leetcode id=3723 lang=cpp
 *
 * [3723] Maximize Sum of Squares of Digits
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string maxSumOfSquares(int n, int s) {
        if (s > n * 9) return "";
        int q = s / 9, r = s % 9;
        string ans = string(q, '9') + (r ? to_string(r) : "");
        ans += string(n - ans.size(), '0');
        return ans;
    }
};
// @lc code=end
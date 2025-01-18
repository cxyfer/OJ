/*
 * @lc app=leetcode.cn id=2582 lang=cpp
 *
 * [2582] 递枕头
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int passThePillow(int n, int time) {
        time %= (n - 1) << 1;
        return time < n ? 1 + time : (n << 1) - time - 1;
    }
};
// @lc code=end
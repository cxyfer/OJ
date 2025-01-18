/*
 * @lc app=leetcode.cn id=2683 lang=cpp
 *
 * [2683] 相邻值的按位异或
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int _xor = 0;
        for (int x : derived) {
            _xor ^= x;
        }
        return _xor == 0;
    }
};
// @lc code=end


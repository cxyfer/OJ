/*
 * @lc app=leetcode.cn id=3151 lang=cpp
 *
 * [3151] Special Array I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            if ((nums[i] & 1) == (nums[i - 1] & 1)) {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=3011 lang=cpp
 *
 * [3011] 判断一个数组是否可以变为有序
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        int n = nums.size(), i = 0, pre_mx = -1;
        while (i < n) {
            int mx = nums[i];
            int cnt = __builtin_popcount(nums[i]);
            while (i < n && __builtin_popcount(nums[i]) == cnt) {
                if (nums[i] < pre_mx) return false;
                mx = max(mx, nums[i]);
                i++;
            }
            pre_mx = mx;
        }
        return true;
    }
};
// @lc code=end
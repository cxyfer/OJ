/*
 * @lc app=leetcode.cn id=80 lang=cpp
 *
 * [80] 删除有序数组中的重复项 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int sz = 2;
        for (int i = 2; i < n; ++i)
            if (nums[sz - 2] != nums[i]) 
                nums[sz++] = nums[i];
        return min(sz, n); // for n = 1
    }
};
// @lc code=end


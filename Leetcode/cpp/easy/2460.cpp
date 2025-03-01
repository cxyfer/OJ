/*
 * @lc app=leetcode id=2460 lang=cpp
 *
 * [2460] Apply Operations to an Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size(), idx = 0;
        for (int i = 0; i < n; ++i) {
            if (i + 1 < n && nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
            if (nums[i] != 0) {
                swap(nums[i], nums[idx++]);
            }
        }
        return nums;
    }
};
// @lc code=end


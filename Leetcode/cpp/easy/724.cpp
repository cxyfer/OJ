/*
 * @lc app=leetcode.cn id=724 lang=cpp
 *
 * [724] 寻找数组的中心下标
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int tot = accumulate(nums.begin(), nums.end(), 0);
        int s = 0;  // prefix sum
        for (int i = 0; i < n; ++i) {
            if (2 * s + nums[i] == tot) return i;
            s += nums[i];
        }
        return -1;
    }
};
// @lc code=end


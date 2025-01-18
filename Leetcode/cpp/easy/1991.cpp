/*
 * @lc app=leetcode.cn id=1991 lang=cpp
 *
 * [1991] 找到数组的中间位置
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
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


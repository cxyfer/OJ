/*
 * @lc app=leetcode.cn id=1509 lang=cpp
 *
 * [1509] 三次操作后最大值与最小值的最小差
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n <= 4) return 0;
        sort(nums.begin(), nums.end());
        int k = n - 3;
        int ans = nums[n - 1] - nums[0];
        for (int i = 0; i <= n - k; i++) {
            int j = i + k - 1;
            ans = min(ans, nums[j] - nums[i]);
        }
        return ans;
    }
};
// @lc code=end
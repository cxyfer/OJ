/*
 * @lc app=leetcode.cn id=3254 lang=cpp
 *
 * [3254] 长度为 K 的子数组的能量值 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans(n - k + 1, -1);
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (i == 0 || nums[i - 1] + 1 == nums[i]) {
                cnt += 1;
            } else {
                cnt = 1;
            }
            if (cnt >= k) {
                ans[i - k + 1] = nums[i];
            }
        }
        return ans;
    }
};
// @lc code=end


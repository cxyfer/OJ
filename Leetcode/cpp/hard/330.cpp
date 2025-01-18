/*
 * @lc app=leetcode.cn id=330 lang=cpp
 *
 * [330] 按要求补齐数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        int m = nums.size(), ans = 0, idx = 0;
        long long s = 0;
        while (s < n) {
            if (idx < m && nums[idx] <= s + 1) {
                s += nums[idx];
                idx++;
            } else {
                s += s + 1;
                ans++;
            }
        }
        return ans;
    }
};
// @lc code=end

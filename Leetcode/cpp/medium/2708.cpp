/*
 * @lc app=leetcode.cn id=2708 lang=cpp
 *
 * [2708] 一个小组的最大实力值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maxStrength(vector<int>& nums) {
        int n = nums.size();
        long long mx = nums[0], mn = nums[0], x, new_mx, new_mn;
        for (int i = 1; i < n; i++) {
            x = nums[i];
            new_mx = max({mx, x, mx * x, mn * x});
            new_mn = min({mn, x, mx * x, mn * x});
            mx = new_mx;
            mn = new_mn;
        }
        return mx;
    }
};
// @lc code=end
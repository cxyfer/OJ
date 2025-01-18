/*
 * @lc app=leetcode.cn id=2848 lang=cpp
 *
 * [2848] 与车相交的点
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {
        sort(nums.begin(), nums.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        vector<vector<int>> intervals;
        for (const auto& interval : nums) {
            if (intervals.empty() || interval[0] > intervals.back()[1]) {
                intervals.push_back(interval);
            } else {
                intervals.back()[1] = max(intervals.back()[1], interval[1]);
            }
        }
        int ans = 0;
        for (const auto& interval : intervals) {
            ans += interval[1] - interval[0] + 1;
        }
        return ans;
    }
};
// @lc code=end
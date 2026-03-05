/*
 * @lc app=leetcode id=56 lang=cpp
 *
 * [56] Merge Intervals
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        ranges::sort(intervals,
                     [](const auto& a, const auto& b) { return a[0] < b[0]; });
        for (const auto& interval : intervals) {
            int l = interval[0], r = interval[1];
            if (ans.empty() || l > ans.back()[1])
                ans.push_back({l, r});
            else
                ans.back()[1] = max(ans.back()[1], r);
        }
        return ans;
    }
};
// @lc code=end

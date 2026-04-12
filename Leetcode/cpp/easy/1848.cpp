/*
 * @lc app=leetcode id=1848 lang=cpp
 *
 * [1848] Minimum Distance to the Target Element
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        return ranges::min(
            views::enumerate(nums) |
            views::filter([&](auto&& p) { return get<1>(p) == target; }) |
            views::transform([&](auto&& p) { return abs(get<0>(p) - start); }));
    }
};
// @lc code=end

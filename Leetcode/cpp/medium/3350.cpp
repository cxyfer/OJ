/*
 * @lc app=leetcode.cn id=3350 lang=cpp
 * @lcpr version=30204
 *
 * [3350] 检测相邻递增子数组 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int ans = 1, pre = 0, cur = 1;
        for (auto [x, y] : views::pairwise(nums)) {
            if (x < y) {
                cur++;
                ans = max({ans, min(pre, cur), cur / 2});
            } else {
                pre = cur;
                cur = 1;
            }
            // ans = max({ans, min(pre, cur), cur / 2});
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,5,7,8,9,2,3,4,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,4,4,4,5,6,7]\n
// @lcpr case=end

 */


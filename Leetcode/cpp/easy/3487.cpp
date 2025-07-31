/*
 * @lc app=leetcode.cn id=3487 lang=cpp
 * @lcpr version=30204
 *
 * [3487] 删除后的最大子数组元素和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    int maxSum(vector<int>& nums) {
        auto pos = nums | views::filter([](int x) { return x > 0; }) |
                   ranges::to<unordered_set>();
        return pos.empty() ? ranges::max(nums)
                           : ranges::fold_left(pos, 0, plus<>());
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,0,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,-1,-2,1,0,-1]\n
// @lcpr case=end

 */


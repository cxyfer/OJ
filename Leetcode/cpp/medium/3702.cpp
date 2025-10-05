/*
 * @lc app=leetcode.cn id=3702 lang=cpp
 * @lcpr version=30204
 *
 * [3702] 按位异或非零的最长子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int n = nums.size();
        if (ranges::fold_left(nums, 0, bit_xor<>{}) != 0)
            return n;
        return (ranges::any_of(nums, [](int x) { return x != 0; }) ? n - 1 : 0);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,4]\n
// @lcpr case=end

 */


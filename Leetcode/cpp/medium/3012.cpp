/*
 * @lc app=leetcode.cn id=3012 lang=cpp
 * @lcpr version=30204
 *
 * [3012] 通过操作使数组长度最小
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int minimumArrayLength(vector<int>& nums) {
        int mn = ranges::min(nums);
        for (int x : nums)
            if (x % mn != 0) // 能構造出更小的數
                return 1;
        return (ranges::count(nums, mn) + 1) >> 1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,4,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [5,5,5,10,5]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,4]\n
// @lcpr case=end

 */


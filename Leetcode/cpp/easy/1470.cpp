/*
 * @lc app=leetcode id=1470 lang=cpp
 * @lcpr version=30112
 *
 * [1470] Shuffle the Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int msk = (1 << 10) - 1;
        for (int i = 0; i < n; i++) {
            nums[i << 1] |= (nums[i] & msk) << 10;
            nums[(i << 1) | 1] |= (nums[i + n] & msk) << 10;
        }
        for (auto& x : nums) x >>= 10;
        return nums;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,5,1,3,4,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,4,3,2,1]\n4\n
// @lcpr case=end

// @lcpr case=start
// [1,1,2,2]\n2\n
// @lcpr case=end

 */


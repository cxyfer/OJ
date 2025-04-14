/*
 * @lc app=leetcode.cn id=3512 lang=cpp
 * @lcpr version=30204
 *
 * [3512] Minimum Operations to Make Array Sum Divisible by K
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        return accumulate(nums.begin(), nums.end(), 0) % k;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,9,7]\n5\n
// @lcpr case=end

// @lcpr case=start
// [4,1,3]\n4\n
// @lcpr case=end

// @lcpr case=start
// [3,2]\n6\n
// @lcpr case=end

 */


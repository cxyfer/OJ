/*
 * @lc app=leetcode.cn id=3024 lang=cpp
 * @lcpr version=30204
 *
 * [3024] 三角形类型
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string triangleType(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if (nums[0] + nums[1] <= nums[2]) return "none";
        else if (nums[0] == nums[2]) return "equilateral";
        else if (nums[0] == nums[1] || nums[1] == nums[2] ) return "isosceles";
        else return "scalene";
    }
};
// @lc code=end


/*
// @lcpr case=start
// [3,3,3]\n
// @lcpr case=end

// @lcpr case=start
// [3,4,5]\n
// @lcpr case=end

 */


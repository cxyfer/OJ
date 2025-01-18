/*
 * @lc app=leetcode id=3028 lang=cpp
 * @lcpr version=30116
 *
 * [3028] Ant on the Boundary
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int ans = 0;
        int cur = 0;
        for (int i = 0; i < nums.size(); i++) {
            cur += nums[i];
            if (cur == 0) {
                ans++;
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,3,-5]\n
// @lcpr case=end

// @lcpr case=start
// [3,2,-3,-4]\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=3354 lang=cpp
 * @lcpr version=30204
 *
 * [3354] 使数组元素等于零
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int tot = accumulate(nums.begin(), nums.end(), 0);
        int ans = 0, s = 0;
        for (int x : nums) {
            if (x != 0) s += x;
            else ans += max(0, 2 - abs(tot - 2 * s));
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,0,2,0,3]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,4,0,4,1,0]\n
// @lcpr case=end

 */


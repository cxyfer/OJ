/*
 * @lc app=leetcode.cn id=3523 lang=cpp
 * @lcpr version=30204
 *
 * [3523] 非递减数组的最大长度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        int n = nums.size();
        int ans = n, pre = nums[0];
        for (int i = 1; i < n; i++) {
            if (pre > nums[i]) ans--;
            else pre = nums[i];
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,2,5,3,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

 */


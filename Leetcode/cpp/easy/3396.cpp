/*
 * @lc app=leetcode.cn id=3396 lang=cpp
 * @lcpr version=30204
 *
 * [3396] 使数组元素互不相同所需的最少操作次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int n = nums.size();
        int idx = n - 1;
        vector<bool> vis(101, false);
        while (idx >= 0 && !vis[nums[idx]])
            vis[nums[idx--]] = true;
        return (idx + 3) / 3;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,2,3,3,5,7]\n
// @lcpr case=end

// @lcpr case=start
// [4,5,6,4,4]\n
// @lcpr case=end

// @lcpr case=start
// [6,7,8,9]\n
// @lcpr case=end

 */


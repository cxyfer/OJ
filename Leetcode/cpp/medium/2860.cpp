/*
 * @lc app=leetcode.cn id=2860 lang=cpp
 * @lcpr version=30204
 *
 * [2860] 让所有学生保持开心的分组方法数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int countWays(vector<int>& nums) {
        int n = nums.size();
        ranges::sort(nums);
        int ans = nums[0] > 0;
        for (int k = 1; k < n; k++)
            if (nums[k - 1] < k && k < nums[k])
                ans++;
        ans += nums[n - 1] < n;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,1]\n
// @lcpr case=end

// @lcpr case=start
// [6,0,3,3,6,7,2,7]\n
// @lcpr case=end

 */


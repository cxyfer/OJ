/*
 * @lc app=leetcode.cn id=2348 lang=cpp
 * @lcpr version=30204
 *
 * [2348] 全 0 子数组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] != 0) continue;
            int j = i;
            while (i < n && nums[i] == 0) ++i;
            ans += (i - j + 1LL) * (i - j) / 2;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,0,0,2,0,0,4]\n
// @lcpr case=end

// @lcpr case=start
// [0,0,0,2,0,0]\n
// @lcpr case=end

// @lcpr case=start
// [2,10,2019]\n
// @lcpr case=end

 */


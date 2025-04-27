/*
 * @lc app=leetcode.cn id=2302 lang=cpp
 * @lcpr version=30204
 *
 * [2302] 统计得分小于 K 的子数组数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        int n = nums.size();
        long long ans = 0, s = 0;
        for (int left = 0, right = 0; right < n; ++right) {
            s += nums[right];
            while (s * (right - left + 1) >= k)
                s -= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,1,4,3,5]\n10\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n5\n
// @lcpr case=end

 */


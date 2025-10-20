/*
 * @lc app=leetcode.cn id=3346 lang=cpp
 * @lcpr version=30204
 *
 * [3346] 执行操作后元素的最高频率 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int n = nums.size();
        ranges::sort(nums);
        unordered_map<int, int> cnt;
        for (auto &x : nums) cnt[x]++;
        int ans = 0;
        for (int v = nums[0]; v <= nums[n - 1]; v++) {
            int l = ranges::lower_bound(nums, v - k) - nums.begin();
            int r = ranges::upper_bound(nums, v + k) - nums.begin();
            ans = max(ans, min(r - l, cnt[v] + numOperations));
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,4,5]\n1\n2\n
// @lcpr case=end

// @lcpr case=start
// [5,11,20,20]\n5\n1\n
// @lcpr case=end

 */


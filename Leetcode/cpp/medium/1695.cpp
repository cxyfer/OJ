/*
 * @lc app=leetcode.cn id=1695 lang=cpp
 * @lcpr version=30204
 *
 * [1695] 删除子数组的最大得分
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int ans = 0, s = 0, left = 0;
        vector<int> cnt(10001);
        for (auto [right, x] : views::enumerate(nums)) {
            s += x;
            cnt[x]++;
            while (cnt[x] > 1) {
                s -= nums[left];
                cnt[nums[left]]--;
                left++;
            }
            ans = max(ans, s);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,2,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// [5,2,1,2,5,2,1,2,5]\n
// @lcpr case=end

 */


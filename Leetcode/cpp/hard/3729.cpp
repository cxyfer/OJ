/*
 * @lc app=leetcode.cn id=3729 lang=cpp
 * @lcpr version=30204
 *
 * [3729] 统计有序数组中可被 K 整除的子数组数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0, s = 0;
        map<int, int> cnt1, cnt2;
        cnt1[0] = 1;
        for (auto [r, x] : views::enumerate(nums)) {
            if (r > 0 and nums[r - 1] != x) cnt2.clear();
            s = (s + x) % k;
            ans += cnt1[s];
            ans -= cnt2[s];
            cnt1[s] += 1;
            cnt2[s] += 1;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n3\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,2,2,2]\n6\n
// @lcpr case=end

 */


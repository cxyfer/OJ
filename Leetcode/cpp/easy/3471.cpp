/*
 * @lc app=leetcode.cn id=3471 lang=cpp
 * @lcpr version=30204
 *
 * [3471] 找出最大的几近缺失整数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == k) return *max_element(nums.begin(), nums.end());
        vector<int> cnt(51, 0);
        for (int x : nums) cnt[x]++;
        int ans = -1;
        for (int i = 0; i < n; (k == 1 ? i++ : i += (n - 1))) {
            if (cnt[nums[i]] == 1) ans = max(ans, nums[i]);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,9,2,1,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [3,9,7,2,1,7]\n4\n
// @lcpr case=end

// @lcpr case=start
// [0,0]\n1\n
// @lcpr case=end

 */


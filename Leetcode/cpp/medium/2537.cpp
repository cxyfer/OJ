/*
 * @lc app=leetcode.cn id=2537 lang=cpp
 * @lcpr version=30204
 *
 * [2537] 统计好子数组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0, cur = 0;
        int left = 0;
        unordered_map<int, int> cnt;
        for (int x : nums) {
            cur += cnt[x]++;
            while (cur >= k) cur -= --cnt[nums[left++]];
            ans += left;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,1,1,1,1]\n10\n
// @lcpr case=end

// @lcpr case=start
// [3,1,4,3,2,2,4]\n2\n
// @lcpr case=end

 */


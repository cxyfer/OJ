/*
 * @lc app=leetcode.cn id=3381 lang=cpp
 * @lcpr version=30204
 *
 * [3381] 长度可被 K 整除的子数组的最大元素和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        long long ans = LLONG_MIN;
        vector<long long> mp(k, LLONG_MAX / 2);
        mp[0] = 0;
        long long s = 0;
        for (int i = 0; i < nums.size(); i++) {
            s += nums[i];
            int m = (i + 1) % k;
            ans = max(ans, s - mp[m]);
            mp[m] = min(mp[m], s);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2]\n1\n
// @lcpr case=end

// @lcpr case=start
// [-1,-2,-3,-4,-5]\n4\n
// @lcpr case=end

// @lcpr case=start
// [-5,1,2,-3,4]\n2\n
// @lcpr case=end

 */


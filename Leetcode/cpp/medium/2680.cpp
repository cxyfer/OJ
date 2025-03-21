/*
 * @lc app=leetcode.cn id=2680 lang=cpp
 * @lcpr version=30204
 *
 * [2680] 最大或值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maximumOr(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> suf(n + 1, 0);
        for (int i = n - 1; i >= 0; i--)
            suf[i] = suf[i + 1] | nums[i];
        long long ans = 0, pre = 0;
        for (int i = 0; i < n; i++) {
            long long x = nums[i];
            ans = max(ans, pre | suf[i + 1] | (x << k));
            pre |= x;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [12,9]\n1\n
// @lcpr case=end

// @lcpr case=start
// [8,1,2]\n2\n
// @lcpr case=end

 */


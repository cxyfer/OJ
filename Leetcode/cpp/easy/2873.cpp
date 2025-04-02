/*
 * @lc app=leetcode.cn id=2873 lang=cpp
 * @lcpr version=30204
 *
 * [2873] 有序三元组中的最大值 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> suf(n);
        suf[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = max(suf[i + 1], nums[i]);
        long long ans = 0;
        int pre_mx = nums[0];
        for (int i = 1; i < n - 1; i++) {
            ans = max(ans, (long long)(pre_mx - nums[i]) * suf[i + 1]);
            pre_mx = max(pre_mx, nums[i]);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [12,6,1,2,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,10,3,4,19]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

 */


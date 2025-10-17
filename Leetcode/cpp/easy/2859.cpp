/*
 * @lc app=leetcode.cn id=2859 lang=cpp
 * @lcpr version=30204
 *
 * [2859] 计算 K 置位下标对应元素的和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
            if (__builtin_popcount(i) == k)
                ans += nums[i];
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [5,10,1,5,2]\n1\n
// @lcpr case=end

// @lcpr case=start
// [4,3,2,1]\n2\n
// @lcpr case=end

 */


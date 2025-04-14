/*
 * @lc app=leetcode.cn id=3514 lang=cpp
 * @lcpr version=30204
 *
 * [3514] 不同 XOR 三元组的数目 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        nums.erase(unique(nums.begin(), nums.end()), nums.end());  // 去重
        int n = nums.size();
        int mx = *max_element(nums.begin(), nums.end());
        int U = 1 << (32 - __builtin_clz(mx));
        vector<bool> pre(U), ans(U);  // 用 vector 代替 set
        pre[0] = ans[nums[0]] = true;
        for (int k = 1; k < n; k++) {
            for (int i = 0; i <= k; i++)  // nums[i] ^ nums[j]
                pre[nums[i] ^ nums[k]] = true;
            for (int i = 0; i < U; i++)  // (nums[i] ^ nums[j]) ^ nums[k]
                if (pre[i]) ans[i ^ nums[k]] = true;
        }
        return count(ans.begin(), ans.end(), true);
    }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3]\n
// @lcpr case=end

// @lcpr case=start
// [6,7,8,9]\n
// @lcpr case=end

 */


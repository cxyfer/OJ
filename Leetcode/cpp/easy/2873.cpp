/*
 * @lc app=leetcode.cn id=2873 lang=cpp
 * @lcpr version=30204
 *
 * [2873] Maximum Value of an Ordered Triplet I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * Greedy
 * 為了找到 (nums[i] - nums[j]) * nums[k] 的最大值
 * 基於貪心思路，可以使 (nums[i] - nums[j]) 和 nums[k] 越大越好
 * 由於需要滿足 i < j < k，所以又有兩種思路：
 * 1. 枚舉 nums[j]，然後找最大的 nums[i] 和 nums[k]，可以透過前後綴分解實現
 * 2. 枚舉 nums[k]，維護前綴中的最大差值 (nums[i] - nums[j])，並維護前綴中最大的 nums[i] 以更新最大差值
 */
// @lc code=start
class Solution1 {
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

class Solution2 {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int mx = LLONG_MIN / 2, mx_diff = LLONG_MIN / 2;
        long long ans = 0;
        for (int x : nums) {
            ans = max(ans, (long long)mx_diff * x);
            mx_diff = max(mx_diff, mx - x);  // (nums[i] - nums[j])
            mx = max(mx, x);  // nums[i]
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
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


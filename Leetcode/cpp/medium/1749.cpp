/*
 * @lc app=leetcode.cn id=1749 lang=cpp
 *
 * [1749] 任意子数组和的绝对值的最大值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        return solve1(nums);
        // return solve2(nums);
    }
    int solve1(vector<int>& nums) {
        int n = nums.size(), res1 = 0, res2 = 0;
        vector<int> dp1(n + 1, 0), dp2(n + 1, 0);
        for (int i = 0; i < n; i++) {
            dp1[i + 1] = max(dp1[i] + nums[i], nums[i]);
            dp2[i + 1] = min(dp2[i] + nums[i], nums[i]);
            res1 = max(res1, dp1[i + 1]);
            res2 = min(res2, dp2[i + 1]);
        }
        return max(res1, abs(res2));
    }
    int solve2(vector<int>& nums) {
        int n = nums.size();
        int f1 = 0, f2 = 0;
        int res1 = 0, res2 = 0;
        for (int i = 0; i < n; i++) {
            f1 = max(f1 + nums[i], nums[i]);
            f2 = min(f2 + nums[i], nums[i]);
            res1 = max(res1, f1);
            res2 = min(res2, f2);
        }
        return max(res1, abs(res2));
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {1,-3,2,3,-4};
    cout << sol.maxAbsoluteSum(nums) << endl; 
    nums = {2,-5,1,-4,3,-2};
    cout << sol.maxAbsoluteSum(nums) << endl;
    return 0;
}


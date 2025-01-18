/*
 * @lc app=leetcode.cn id=643 lang=cpp
 *
 * [643] 子数组最大平均数 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MIN, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += nums[i];
            if (i < k - 1) continue;
            ans = max(ans, cur);
            cur -= nums[i - k + 1];
        }
        return ans / (double)k;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {1, 12, -5, -6, 50, 3};
    int k = 4;
    cout << sol.findMaxAverage(nums, k) << endl;
    cout << DBL_MIN << endl;
    return 0;
}
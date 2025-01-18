/*
 * @lc app=leetcode.cn id=2786 lang=cpp
 *
 * [2786] 访问数组中的位置使分数最大
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int INF = 0x3f3f3f3f;
class Solution {
public:
    long long maxScore(vector<int>& nums, int x) {
        // return solve1(nums, x);
        return solve2(nums, x);
    }
    long long solve1(vector<int>& nums, int x) {
        int n = nums.size();
        long long ans = nums[0];
        vector<vector<long long>> dp(n, vector<long long>(2, -INF));
        dp[0][nums[0] % 2] = nums[0];
        for (int i = 1; i < n; i++) {
            int p = nums[i] % 2;
            dp[i][p] = max(dp[i - 1][p] + nums[i], dp[i - 1][1 - p] + nums[i] - x);
            dp[i][1 - p] = dp[i - 1][1 - p];
            ans = max(ans, dp[i][p]);
        }
        return ans;
    }
    long long solve2(vector<int>& nums, int x) {
        int n = nums.size();
        long long ans = nums[0];
        vector<long long> dp(2, -INF);
        dp[nums[0] % 2] = nums[0];
        for (int i = 1; i < n; i++) {
            int p = nums[i] % 2;
            dp[p] = max(dp[p] + nums[i], dp[1 - p] + nums[i] - x);
            ans = max(ans, dp[p]);
        }
        return ans;
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<int> nums = {8,50,65,85,8,73,55,50,29,95,5,68,52,79};
    cout << sol.maxScore(nums, 74) << endl;
    return 0;
}
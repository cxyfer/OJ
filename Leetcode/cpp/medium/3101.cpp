/*
 * @lc app=leetcode.cn id=3101 lang=cpp
 *
 * [3101] 交替子数组计数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long countAlternatingSubarrays(vector<int>& nums) {
        int n = nums.size();
        long long ans = 1;
        vector<int> dp(n, 1);
        for (int i = 1; i < n; i++) {
            if (nums[i] != nums[i - 1]) dp[i] = dp[i - 1] + 1;
            ans += dp[i];
        }
        return ans;
    }
};

class Solution2 {
public:
    long long countAlternatingSubarrays(vector<int>& nums) {
        int n = nums.size();
        long long ans = 1;
        int f = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] != nums[i - 1]) f += 1;
            else f = 1;
            ans += f;
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end


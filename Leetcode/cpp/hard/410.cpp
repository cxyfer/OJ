/*
 * @lc app=leetcode.cn id=410 lang=cpp
 *
 * [410] 分割数组的最大值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int splitArray(vector<int>& nums, int k) {
        
        auto check = [&](int d) -> bool {
            int s = 0, cnt = 1;
            for (int x : nums) {
                if (s + x > d) {
                    cnt++;
                    s = x;
                } else {
                    s += x;
                }
            }
            return cnt <= k;
        };

        int left = *max_element(nums.begin(), nums.end());
        int right = accumulate(nums.begin(), nums.end(), 0);
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};

class Solution2a {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> s(n + 1, 0); // prefix sum
        for (int i = 0; i < n; i++) s[i+1] = s[i] + nums[i];

        vector<vector<int>> memo(n + 1, vector<int>(k + 1, INT_MAX));
        function<int(int, int)> dfs = [&](int i, int j) -> int {
            if (j == 1) return s[i];
            if (j > i) return INT_MAX;
            int& res = memo[i][j];
            if (res != INT_MAX) return res;
            for (int x = 0; x < i; x++) {
                res = min(res, max(dfs(x, j - 1), s[i] - s[x]));
            }
            return res;
        };
        return dfs(n, k);
    }
};

class Solution2b {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> s(n + 1, 0); // prefix sum
        for (int i = 0; i < n; i++) s[i+1] = s[i] + nums[i];

        vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= min(i, k); j++)
                for (int x = 0; x < i; x++)
                    dp[i][j] = min(dp[i][j], max(dp[x][j - 1], s[i] - s[x]));
        return dp[n][k];
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2a {};
// class Solution : public Solution2b {};
// @lc code=end
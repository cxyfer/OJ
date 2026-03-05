/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> memo(n, -1);
        auto dfs = [&](this auto&& dfs, int i) -> int {
            if (i < 0) return 0;
            if (memo[i] != -1) return memo[i];
            return memo[i] = max(dfs(i - 2) + nums[i], dfs(i - 1));
        };
        return dfs(n - 1);
    }
};

class Solution2 {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> f(n + 2, 0);
        for (int i = 2; i <= n + 1; i++)
            f[i] = max(f[i - 2] + nums[i - 2], f[i - 1]);
        return f[n + 1];
    }
};

class Solution3 {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int f0 = 0, f1 = 0;
        for (int x : nums)
            tie(f0, f1) = tuple(f1, max(f0 + x, f1));
        return f1;
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
using Solution = Solution3;
// @lc code=end

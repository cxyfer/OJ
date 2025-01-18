/*
 * @lc app=leetcode id=3176 lang=cpp
 *
 * [3176] Find the Maximum Length of a Good Subsequence I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> memo(n, vector<int>(k + 1, -1));
        function<int(int, int)> dfs = [&](int i, int k) -> int {
            if (k < 0) return 0;
            if (i == 0) return 1;
            if (memo[i][k] != -1) return memo[i][k];
            int res = 0;
            for (int j = i - 1; j >= 0; j--) {  // 枚舉前一個數字
                if (nums[j] != nums[i]) // 消耗一次 k
                    res = max(res, 1 + dfs(j, k - 1));
                else
                    res = max(res, 1 + dfs(j, k));
            }
            return memo[i][k] = res;
        };
        int ans = 0;
        for (int i = 0; i < n; i++) ans = max(ans, dfs(i, k));
        return ans;
    }
};
// @lc code=end
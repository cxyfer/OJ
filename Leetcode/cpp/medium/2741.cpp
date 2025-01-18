/*
 * @lc app=leetcode.cn id=2741 lang=cpp
 *
 * [2741] 特别的排列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    const int MOD = 1e9 + 7;
    int specialPerm(vector<int>& nums) {
        int n = nums.size();
        int u = (1 << n) - 1;
        
        vector<vector<int>> memo(1 << n, vector<int>(n, -1));
        function<int(int, int)> dfs = [&](int s, int i) -> int {
            if (s == u) return 1;
            if (memo[s][i] != -1) return memo[s][i];
            int res = 0;
            for (int j = 0; j < n; j++) {
                if ((s >> j) & 1) continue;
                if (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0) {
                    res = (res + dfs(s | (1 << j), j)) % MOD;
                }
            }
            return memo[s][i] = res;
        };

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + dfs(1 << i, i)) % MOD;
        }
        return ans;
    }
};
// @lc code=end
/*
 * @lc app=leetcode id=3193 lang=cpp
 *
 * [3193] Count the Number of Inversions
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    const int MOD = 1e9 + 7;
    int numberOfPermutations(int n, vector<vector<int>>& requirements) {
        unordered_map<int, int> mp;
        for (auto& r : requirements) {
            mp[r[0]] = r[1];
        }
        vector<vector<int>> dp(n + 1, vector<int>(401, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            int mn = (mp.find(i - 1) != mp.end()) ? mp[i - 1] : 0;
            int mx = (mp.find(i - 1) != mp.end()) ? mp[i - 1] : 400;
            for (int j = mn; j <= mx; j++) {
                for (int k = 0; k < min(i, j + 1); k++) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < 401; i++) {
            ans = (ans + dp[n][i]) % MOD;
        }
        return ans;
    }
};
// @lc code=end


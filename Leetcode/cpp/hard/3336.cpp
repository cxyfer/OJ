/*
 * @lc app=leetcode id=3336 lang=cpp
 *
 * [3336] Find the Number of Subsequences With Equal GCD
 */


// @lcpr-template-start
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
const int MAX_V = 200;

vector<vector<int>> g(MAX_V + 1, vector<int>(MAX_V + 1, 0));

auto init = []() {
    for (int i = 0; i <= MAX_V; ++i)
        for (int j = 0; j <= i; ++j) g[i][j] = g[j][i] = (j ? g[j][i % j] : i);
    return 0;
}();

class Solution {
public:
    int subsequencePairCount(vector<int>& nums) {
        int U = ranges::max(nums);
        vector<vector<int>> f(U + 1, vector<int>(U + 1, 0));
        f[0][0] = 1;
        for (auto x : nums) {
            auto nf = f;
            for (int g1 = 0; g1 <= U; ++g1) {
                for (int g2 = 0; g2 <= U; ++g2) {
                    int val = f[g1][g2];
                    if (val == 0) continue;
                    nf[g[g1][x]][g2] = (nf[g[g1][x]][g2] + val) % MOD;
                    nf[g1][g[g2][x]] = (nf[g1][g[g2][x]] + val) % MOD;
                }
            }
            f = move(nf);
        }

        int ans = 0;
        for (int g = 1; g <= U; ++g) ans = (ans + f[g][g]) % MOD;
        return ans;
    }
};
// @lc code=end
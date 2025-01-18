/*
 * @lc app=leetcode.cn id=3068 lang=cpp
 *
 * [3068] 最大节点价值之和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    LL maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        // return solve1(nums, k, edges);
        // return solve2a(nums, k, edges);
        return solve2b(nums, k, edges);
    }
    LL solve1(vector<int>& nums, int k, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> g(n); // adjacency list
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        function<pair<LL, LL>(int, int)> dfs = [&](int u, int fa) -> pair<LL, LL> {
            LL f0 = 0, f1 = LLONG_MIN; // f0/f1: 在 u 操作偶數/奇數次時，其子樹(不包括 u)的最大值，即 f(u, 0) 和 f(u, 1)
            for (int v : g[u]) {
                if (v == fa) continue;
                pair<LL, LL> p = dfs(v, u);
                LL r0 = p.first, r1 = p.second; // 不操作/操作 (v, u) 這條邊時，v 的子樹(包含 v) 的最大值
                LL t0 = f0, t1 = f1; // backup
                f0 = max(t0 + r0, t1 + r1); // 不操作/操作 (u, v) 這條邊
                f1 = max(t0 + r1, t1 + r0); // 不操作/操作 (u, v) 這條邊
            }
            return make_pair(max(f0 + nums[u], f1 + (nums[u] ^ k)), max(f1 + nums[u], f0 + (nums[u] ^ k))); // 不操作/操作 (u, fa) 這條邊
        };
        return dfs(0, -1).first;
    }
    LL solve2a(vector<int>& nums, int k, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<LL>> dp(n + 1, {0, LLONG_MIN}); // dp[i][0/1]: 前 i 個點總共操作偶數/奇數次時的最大值
        for (int i = 0; i < n; i++) {
            dp[i + 1][0] = max(dp[i][0] + nums[i], dp[i][1] + (nums[i] ^ k)); // 當前點不操作/操作
            dp[i + 1][1] = max(dp[i][1] + nums[i], dp[i][0] + (nums[i] ^ k)); // 當前點不操作/操作
        }
        return dp[n][0];
    }
    LL solve2b(vector<int>& nums, int k, vector<vector<int>>& edges) {
        LL f0 = 0, f1 = LLONG_MIN; // f0/f1: 總共操作偶數/奇數次時的最大值
        for (int x : nums) {
            LL t0 = f0, t1 = f1; // backup
            f0 = max(t0 + x, t1 + (x ^ k)); // 不操作/操作
            f1 = max(t1 + x, t0 + (x ^ k)); // 不操作/操作
        }
        return f0;
    }
};
// @lc code=end


/*
 * @lc app=leetcode id=2467 lang=cpp
 *
 * [2467] Most Profitable Path in a Tree
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        
        vector<int> bobTime(n, INT_MAX / 2);
        auto dfs_bob = [&](auto &&dfs_bob, int u, int fa, int t) -> bool {
            if (u == 0) {
                bobTime[u] = t;
                return true;
            }
            for (auto v : g[u]) {
                if (v == fa) continue;
                if (dfs_bob(dfs_bob, v, u, t + 1)) {
                    bobTime[u] = t;
                    return true;
                }
            }
            return false;
        };
        dfs_bob(dfs_bob, bob, -1, 0);

        int ans = INT_MIN / 2;
        auto dfs_alice = [&](auto &&dfs_alice, int u, int fa, int t, int cur) -> void {
            if (t < bobTime[u]) cur += amount[u];
            else if (t == bobTime[u]) cur += amount[u] / 2;

            bool is_leaf = true;
            for (auto v : g[u]) {
                if (v == fa) continue;
                is_leaf = false;
                dfs_alice(dfs_alice, v, u, t + 1, cur);
            }
            if (is_leaf) ans = max(ans, cur);
        };
        dfs_alice(dfs_alice, 0, -1, 0, 0);
        return ans;
    }
};
// @lc code=end


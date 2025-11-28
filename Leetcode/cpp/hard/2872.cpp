/*
 * @lc app=leetcode.cn id=2872 lang=cpp
 * @lcpr version=30204
 *
 * [2872] 可以被 K 整除连通块的最大数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 0;
        auto dfs = [&](this auto&& dfs, int u, int fa) -> int {
            int s = values[u] % k;
            for (auto v : g[u]) {
                if (v == fa) continue;
                s = (s + dfs(v, u)) % k;
            }
            ans += (s == 0);
            return s;
        };
        dfs(0, -1);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n[[0,2],[1,2],[1,3],[2,4]]\n[1,8,1,4,4]\n6\n
// @lcpr case=end

// @lcpr case=start
// 7\n[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]\n[3,0,6,1,5,2,1]\n3\n
// @lcpr case=end

 */


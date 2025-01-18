/*
 * @lc app=leetcode id=834 lang=cpp
 * @lcpr version=30122
 *
 * [834] Sum of Distances in Tree
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        vector<int> ans(n, 0);
        vector<int> sz(n, 1); // size

        function<void(int, int, int)> dfs = [&](int u, int fa, int depth) {
            ans[0] += depth;
            for (int v : g[u]) {
                if (v == fa) continue;
                dfs(v, u, depth + 1);
                sz[u] += sz[v];
            }
        };
        dfs(0, -1, 0);

        function<void(int, int)> reroot = [&](int u, int fa) {
            for (int v : g[u]) {
                if (v == fa) continue;
                ans[v] = ans[u] - sz[v] + n - sz[v];
                reroot(v, u);
            }
        };
        reroot(0, -1);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]\n
// @lcpr case=end

// @lcpr case=start
// 1\n[]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[[1,0]]\n
// @lcpr case=end

 */


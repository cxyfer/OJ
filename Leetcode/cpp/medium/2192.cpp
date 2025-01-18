/*
 * @lc app=leetcode.cn id=2192 lang=cpp
 *
 * [2192] 有向无环图中一个节点的所有祖先
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
        }

        vector<vector<int>> ans(n);
        vector<bool> visited(n, false);
        
        function<void(int, int)> dfs = [&](int st, int u) {
            for (int v : g[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    ans[v].push_back(st);
                    dfs(st, v);
                }
            }
        };

        for (int st = 0; st < n; ++st) {
            fill(visited.begin(), visited.end(), false);
            dfs(st, st);
        }
        return ans;
    }
};
// @lc code=end
/*
 * @lc app=leetcode.cn id=2065 lang=cpp
 *
 * [2065] 最大化一张图中的路径价值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximalPathQuality(vector<int>& values, vector<vector<int>>& edges, int maxTime) {
        int n = values.size();
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].emplace_back(e[1], e[2]);
            g[e[1]].emplace_back(e[0], e[2]);
        }

        int ans = 0;
        vector<bool> visited(n, false);
        function<void(int, int, int)> dfs = [&](int u, int time, int quality) {
            if (u == 0) ans = max(ans, quality);
            for (auto& [v, t] : g[u]) {
                if (time + t > maxTime) continue;
                if (!visited[v]) {
                    visited[v] = true;
                    dfs(v, time + t, quality + values[v]);
                    visited[v] = false;
                } else {
                    dfs(v, time + t, quality);
                }
            }
        };
        visited[0] = true;
        dfs(0, 0, values[0]);
        return ans;
    }
};
// @lc code=end
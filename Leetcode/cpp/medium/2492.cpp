/*
 * @lc app=leetcode.cn id=2492 lang=cpp
 * @lcpr version=30204
 *
 * [2492] 两个城市间路径的最小分数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& r : roads) {
            int u = r[0] - 1, v = r[1] - 1, w = r[2];
            g[u].emplace_back(v, w);
            g[v].emplace_back(u, w);
        }

        int ans = INT_MAX;
        queue<int> q;
        vector<bool> vis(n);
        q.push(0);
        vis[0] = true;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto [v, w] : g[u]) {
                ans = min(ans, w);
                if (!vis[v]) {
                    vis[v] = true;
                    q.push(v);
                }
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 4\n[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[[1,2,2],[1,3,4],[3,4,7]]\n
// @lcpr case=end

 */


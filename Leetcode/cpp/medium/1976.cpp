/*
 * @lc app=leetcode.cn id=1976 lang=cpp
 * @lcpr version=30204
 *
 * [1976] Number of Ways to Arrive at Destination
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
using pll = pair<LL, LL>;
const int MOD = 1e9 + 7;

class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& r : roads) {
            g[r[0]].emplace_back(r[1], r[2]);
            g[r[1]].emplace_back(r[0], r[2]);
        }

        vector<LL> dist(n, LLONG_MAX / 2);
        vector<int> ans(n, 0);
        dist[0] = 0;
        ans[0] = 1;
        priority_queue<pll, vector<pll>, greater<pll>> pq;
        pq.emplace(0, 0);
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (dist[u] < d) continue;
            for (auto [v, w] : g[u]) {
                LL nd = dist[u] + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    ans[v] = ans[u];
                    pq.emplace(nd, v);
                } else if (nd == dist[v]) {
                    ans[v] = (ans[u] + ans[v]) % MOD;
                }
            }
        }
        return ans[n - 1];
    }
};
// @lc code=end



/*
// @lcpr case=start
// 7\n[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[[1,0,10]]\n
// @lcpr case=end

 */


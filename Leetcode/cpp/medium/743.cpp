/*
 * @lc app=leetcode.cn id=743 lang=cpp
 *
 * [743] 网络延迟时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& t : times) {
            g[t[0] - 1].emplace_back(t[1] - 1, t[2]);
        }
        vector<int> dist(n, INT_MAX);
        dist[k - 1] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> hp;
        hp.emplace(0, k - 1);
        while (!hp.empty()) {
            auto [d, u] = hp.top();
            hp.pop();
            if (d > dist[u]) continue;
            for (auto [v, w] : g[u]) {
                int new_d = d + w;
                if (new_d < dist[v]) {
                    dist[v] = new_d;
                    hp.emplace(new_d, v);
                }
            }
        }
        int ans = *max_element(dist.begin(), dist.end());
        return ans == INT_MAX ? -1 : ans;
    }
};
// @lc code=end


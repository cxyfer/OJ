/*
 * @lc app=leetcode.cn id=2359 lang=cpp
 *
 * [2359] 找到离给定两个节点最近的节点
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        auto get_dist = [&](int u) -> vector<int> {
            vector<int> dist(n, INT_MAX);
            int d = 0;
            while (u != -1 && dist[u] == INT_MAX) {
                dist[u] = d++;
                u = edges[u];
            }
            return dist;
        };
        auto dist1 = get_dist(node1);
        auto dist2 = get_dist(node2);
        int ans = -1, min_dist = INT_MAX;
        for (int i = 0; i < n; i++) {
            int d = max(dist1[i], dist2[i]);
            if (d < min_dist) {
                min_dist = d;
                ans = i;
            }
        }
        return ans;
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=2045 lang=cpp
 *
 * [2045] 到达目的地的第二短时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            int u = e[0]-1, v = e[1]-1;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        
        vector<vector<int>> dis(n, vector<int>(2, INT_MAX / 2));
        dis[0][0] = 0;
        deque<pair<int, int>> q;
        q.push_back({0, 0});
        while (!q.empty()) {
            int u = q.front().first, d = q.front().second;
            q.pop_front();
            int sw = d / change;
            int nd = sw & 1? (sw + 1) * change + time : d + time;
            for (int v : g[u]) {
                if (dis[v][0] > nd) {
                    dis[v][0] = nd;
                    q.push_back({v, nd});
                }
                else if (dis[v][0] < nd && dis[v][1] > nd) {
                    dis[v][1] = nd;
                    q.push_back({v, nd});
                }
            }
        }
        return dis[n-1][1];
    }
};
// @lc code=end

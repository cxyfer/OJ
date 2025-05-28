/*
 * @lc app=leetcode.cn id=3372 lang=cpp
 * @lcpr version=30204
 *
 * [3372] 连接两棵树后最大目标节点数目 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n1 = edges1.size() + 1, n2 = edges2.size() + 1;
        vector<vector<int>> g1(n1), g2(n2);
        for (auto& e : edges1) {
            g1[e[0]].push_back(e[1]);
            g1[e[1]].push_back(e[0]);
        }
        for (auto& e : edges2) {
            g2[e[0]].push_back(e[1]);
            g2[e[1]].push_back(e[0]);
        }

        auto bfs = [&](int u, int t, vector<vector<int>>& g) {
            int n = g.size(), cnt = 0;
            queue<int> q;
            q.push(u);
            vector<int> dist(n, INT_MAX / 2);
            dist[u] = 0;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                if (dist[u] > t) break;
                cnt += 1;
                for (int v : g[u]) {
                    if (dist[u] + 1 < dist[v]) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return cnt;
        };

        vector<int> ans(n1, 0), cnt2(n2, 0);
        for (int u = 0; u < n2; u++)
            cnt2[u] = bfs(u, k - 1, g2);
        int mx2 = *max_element(cnt2.begin(), cnt2.end());
        for (int u = 0; u < n1; u++)
            ans[u] = bfs(u, k, g1) + mx2;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[0,1],[0,2],[2,3],[2,4]]\n[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[0,1],[0,2],[0,3],[0,4]]\n[[0,1],[1,2],[2,3]]\n1\n
// @lcpr case=end

 */


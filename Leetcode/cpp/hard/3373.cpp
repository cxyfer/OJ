/*
 * @lc app=leetcode.cn id=3373 lang=cpp
 * @lcpr version=30204
 *
 * [3373] 连接两棵树后最大目标节点数目 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1, m = edges2.size() + 1;
        vector<vector<int>> g1(n), g2(m);
        for (auto& e : edges1) {
            g1[e[0]].push_back(e[1]);
            g1[e[1]].push_back(e[0]);
        }
        for (auto& e : edges2) {
            g2[e[0]].push_back(e[1]);
            g2[e[1]].push_back(e[0]);
        }

        auto bfs = [&](vector<vector<int>>& g, vector<int>& dist, vector<int>& cnt) -> void {
            queue<int> q;
            q.push(0);
            dist[0] = 0;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                int d = dist[u];
                cnt[d & 1] += 1;
                for (int v : g[u]) {
                    if (d + 1 < dist[v]) {
                        dist[v] = d + 1;
                        q.push(v);
                    }
                }
            }
            return;
        };

        vector<int> dist1(n, INT_MAX / 2), dist2(m, INT_MAX / 2);
        vector<int> cnt1(2, 0), cnt2(2, 0);
        bfs(g1, dist1, cnt1);
        bfs(g2, dist2, cnt2);
        int mx2 = *max_element(cnt2.begin(), cnt2.end());
        vector<int> ans(n, 0);
        for (int u = 0; u < n; u++)
            ans[u] = cnt1[dist1[u] & 1] + mx2;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[0,1],[0,2],[2,3],[2,4]]\n[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,1],[0,2],[0,3],[0,4]]\n[[0,1],[1,2],[2,3]]\n
// @lcpr case=end

 */


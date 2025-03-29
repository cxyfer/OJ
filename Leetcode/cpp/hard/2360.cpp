/*
 * @lc app=leetcode.cn id=2360 lang=cpp
 * @lcpr version=30204
 *
 * [2360] 图中的最长环
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int longestCycle(vector<int>& edges) {
        int n = edges.size();
        vector<int> ind(n, 0);
        for (int u = 0; u < n; u++)
            if (edges[u] != -1)
                ind[edges[u]]++;
   
        queue<int> q;
        for (int u = 0; u < n; u++)
            if (ind[u] == 0)
                q.push(u);
        
        while (!q.empty()) {
            int u = q.front(); q.pop();
            int v = edges[u];
            if (v == -1) continue;
            ind[v]--;
            if (ind[v] == 0)
                q.push(v);
        }

        int ans = -1;
        vector<bool> vis(n, false);
        for (int u = 0; u < n; u++) {
            if (ind[u] == 0 or edges[u] == -1) continue;
            int cnt = 1;
            int v = edges[u];
            ind[u] = ind[v] = 0;
            while (v != u) {
                cnt++;
                v = edges[v];
                ind[v] = 0;
            }
            ans = max(ans, cnt);
        }
        return ans;
    }
};
// @lc code=end

/*
// @lcpr case=start
// [3,3,4,2]\n[2,-1,3,1]\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=3067 lang=cpp
 *
 * [3067] 在带权树网络中统计可连接服务器对数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        DFS + 乘法原理
        Similar to 2867. Count Valid Paths in a Tree
    */
    vector<int> countPairsOfConnectableServers(vector<vector<int>>& edges, int signalSpeed) {
        int n = edges.size() + 1; // 注意樹中點的數量是邊數加一
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].emplace_back(e[1], e[2]);
            g[e[1]].emplace_back(e[0], e[2]);
        }

        function <int(int, int, int)> dfs = [&](int u, int fa, int ps) -> int { // ps 是與根節點的距離
            int res = ps % signalSpeed == 0; // 與根節點距離是 signalSpeed 的倍數的節點數
            for (auto& vw: g[u]) {
                int v = vw.first, w = vw.second;
                if (v == fa) continue;
                res += dfs(v, u, ps + w);
            }
            return res;
        };

        vector<int> ans(n);
        for (int u = 0; u < n; u++) { // 枚舉每個節點作為根節點
            int pre = 0; // 前面子樹中符合條件的節點數
            for (auto& vw: g[u]) {
                int v = vw.first, w = vw.second;
                int cur = dfs(v, u, w); // 以 v 為根的子樹，符合條件的節點數
                ans[u] += pre * cur; // 乘法原理
                pre += cur;
            }
        }
        return ans;
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=3108 lang=cpp
 * @lcpr version=30204
 *
 * [3108] 带权图里旅途的最小代价
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        vector<int> pa(n), sz(n, 1), ands(n, 0xFFFFFFFF);
        iota(pa.begin(), pa.end(), 0);

        auto find = [&](int x) -> int {
            while (x != pa[x]) {
                pa[x] = pa[pa[x]];
                x = pa[x];
            }
            return x;
        };

        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            int fx = find(u), fy = find(v);
            ands[fx] &= w;
            if (fx == fy) continue;
            if (sz[fx] < sz[fy]) swap(fx, fy);
            sz[fx] += sz[fy];
            ands[fx] &= ands[fy];
            pa[fy] = fx;
        }

        vector<int> ans;
        for (auto& q : query) {
            int u = q[0], v = q[1];
            int fx = find(u), fy = find(v);
            ans.push_back(fx == fy ? ands[fx] : -1);
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }

        vector<int> idxs(n, -1);
        vector<int> ands;
        auto dfs = [&](auto &&dfs, int u) -> int {
            int res = 0xFFFFFFFF;
            idxs[u] = ands.size();
            for (auto& [v, w] : g[u]) {
                res &= w;
                if (idxs[v] >= 0) continue;
                res &= dfs(dfs, v);
            }
            return res;
        };

        for (int i = 0; i < n; i++) {
            if (idxs[i] >= 0) continue;
            ands.push_back(dfs(dfs, i));
        }

        vector<int> ans;
        for (auto& q : query) {
            int u = q[0], v = q[1];
            ans.push_back(idxs[u] == idxs[v] ? ands[idxs[u]] : -1);
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end



/*
// @lcpr case=start
// 5\n[[0,1,7],[1,3,7],[1,2,1]]\n[[0,3],[3,4]]\n
// @lcpr case=end

// @lcpr case=start
// 3\n[[0,2,7],[0,1,15],[1,2,6],[1,2,1]]\n[[1,2]]\n
// @lcpr case=end

 */


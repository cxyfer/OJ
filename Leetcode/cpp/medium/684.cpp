/*
 * @lc app=leetcode.cn id=684 lang=cpp
 *
 * [684] 冗余连接
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> pa(n + 1);
        vector<int> sz(n + 1, 1);
        for (int i = 0; i < n + 1; ++i) pa[i] = i;

        function<int(int)> find = [&](int x) -> int {
            if (pa[x] != x) pa[x] = find(pa[x]);
            return pa[x];
        };

        for (auto& e : edges) {
            int fx = find(e[0]), fy = find(e[1]);
            if (fx == fy) return e;
            if (sz[fx] > sz[fy]) swap(fx, fy);
            pa[fy] = fx;
            sz[fx] += sz[fy];
        }
        return {};
    }
};
// @lc code=end


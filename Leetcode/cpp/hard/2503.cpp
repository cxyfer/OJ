/*
 * @lc app=leetcode.cn id=2503 lang=cpp
 * @lcpr version=30204
 *
 * [2503] 矩阵查询可获得的最大分数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class UnionFind {
public:
    vector<int> pa, sz;
    int cnt;
    UnionFind(int n) {
        pa.resize(n);
        iota(pa.begin(), pa.end(), 0);
        sz.assign(n, 1);
        cnt = n;
    }
    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }
    bool unionSet(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) return false;
        if (sz[x] < sz[y]) swap(x, y);
        pa[y] = x;
        sz[x] += sz[y];
        cnt--;
        return true;
    }
};

class Solution {
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int m = grid.size(), n = grid[0].size(), q = queries.size();
        UnionFind uf(m * n);
        vector<tuple<int, int, int>> edges;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i + 1 < m) edges.emplace_back(max(grid[i][j], grid[i + 1][j]), i * n + j, (i + 1) * n + j);
                if (j + 1 < n) edges.emplace_back(max(grid[i][j], grid[i][j + 1]), i * n + j, i * n + j + 1);
            }
        }
        sort(edges.begin(), edges.end());

        vector<int> qidxs(q);
        iota(qidxs.begin(), qidxs.end(), 0);
        sort(qidxs.begin(), qidxs.end(), [&](int i, int j) {
            return queries[i] < queries[j];
        });

        int idx = 0;
        vector<int> ans(q);
        for (auto& qi : qidxs) {
            int query = queries[qi];
            while (idx < edges.size() && get<0>(edges[idx]) < query) {
                auto [w, x, y] = edges[idx++];
                uf.unionSet(x, y);
            }
            ans[qi] = grid[0][0] < query ? uf.sz[uf.find(0)] : 0;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[2,5,7],[3,5,1]]\n[5,6,2]\n
// @lcpr case=end

// @lcpr case=start
// [[5,2,1],[1,1,2]]\n[3]\n
// @lcpr case=end

 */


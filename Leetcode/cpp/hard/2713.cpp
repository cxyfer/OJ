/*
 * @lc app=leetcode.cn id=2713 lang=cpp
 *
 * [2713] 矩阵中严格递增的单元格数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        map<int, vector<pair<int, int>>> g;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                g[mat[i][j]].push_back({i, j});
            }
        }
        vector<int> row_max(m, 0), col_max(n, 0);
        for (auto& kv : g) {
            auto& pos = kv.second;
            vector<int> res; // 要先把轉移的結果算出來，否則會被覆蓋
            for (auto& ij : pos) {
                int i = ij.first, j = ij.second;
                res.push_back(max(row_max[i], col_max[j]) + 1);
            }
            for (int k = 0; k < pos.size(); k++) {
                int i = pos[k].first, j = pos[k].second;
                row_max[i] = max(row_max[i], res[k]);
                col_max[j] = max(col_max[j], res[k]);
            }
        }
        return *max_element(row_max.begin(), row_max.end());
    }
};
// @lc code=end


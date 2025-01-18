/*
 * @lc app=leetcode.cn id=2392 lang=cpp
 *
 * [2392] 给定条件下构造矩阵
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        vector<int> row, col;
        row = topological_sort(k, rowConditions);
        col = topological_sort(k, colConditions);
        if (row.empty() || col.empty()) return {};
        vector<vector<int>> ans(k, vector<int>(k, 0));
        for (int x = 0; x < k; x++) { // x 在第 i 橫列，第 j 直行
            ans[row[x]][col[x]] = x + 1;
        }
        return ans;
    }
    vector<int> topological_sort(int k, vector<vector<int>>& conditions) {
        vector<vector<int>> g(k); // adjacency list
        vector<int> deg(k); // in-degree
        for (auto &e : conditions) {
            int x = e[0], y = e[1];
            g[x - 1].push_back(y - 1);
            deg[y - 1]++;
        }
        vector<int> order; // 拓樸排序的結果，第 i 個元素是 x
        deque<int> q;
        for (int i = 0; i < k; i++) {
            if (deg[i] == 0) q.push_back(i);
        }
        while (!q.empty()) {
            int x = q.front(); q.pop_front();
            order.push_back(x);
            for (int y : g[x]) {
                deg[y]--;
                if (deg[y] == 0) q.push_back(y);
            }
        }
        if (order.size() != k) return {};
        vector<int> pos(k); // 把「第 i 個元素是 x」轉換為「x 在第 i 個位置」
        for (int i = 0; i < k; i++) pos[order[i]] = i;
        return pos;
    }
};
// @lc code=end
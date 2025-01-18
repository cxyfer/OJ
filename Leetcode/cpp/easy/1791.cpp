/*
 * @lc app=leetcode.cn id=1791 lang=cpp
 *
 * [1791] 找出星型图的中心节点
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<int> deg(n + 1, 0);
        for (auto edge : edges) {
            int u = edge[0], v = edge[1];
            deg[u]++;
            deg[v]++;
        }
        for (int i = 1; i <= n; i++) {
            if (deg[i] == n - 1) return i;
        }
        return -1;
    }
};
// @lc code=end


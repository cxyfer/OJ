/*
 * @lc app=leetcode.cn id=2924 lang=cpp
 *
 * [2924] 找到冠军 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int> ind(n, 0);
        for (auto& e: edges) {
            ind[e[1]]++;
        }
        int ans = -1;
        for (int u = 0; u < n; ++u) {
            if (ind[u] != 0) continue;
            if (ans != -1) return -1;
            ans = u;
        }
        return ans;
    }
};
// @lc code=end


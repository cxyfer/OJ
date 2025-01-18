/*
 * @lc app=leetcode.cn id=2246 lang=cpp
 *
 * [2246] 相邻字符不同的最长路径
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> g(n);
        for (int i = 1; i < n; ++i) {
            g[parent[i]].push_back(i);
        }
        int ans = 0;
        auto dfs = [&](auto&& dfs, int u) -> int {
            int first = 0, second = 0;
            for (int v : g[u]) {
                int length = dfs(dfs, v);
                if (s[u] == s[v]) continue;
                if (length > first) {
                    second = first;
                    first = length;
                } else if (length > second) {
                    second = length;
                }
            }
            ans = max(ans, first + second + 1);
            return first + 1;
        };
        dfs(dfs, 0);
        return ans;
    }
};
// @lc code=end


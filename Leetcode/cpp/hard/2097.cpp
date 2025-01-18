/*
 * @lc app=leetcode.cn id=2097 lang=cpp
 *
 * [2097] 合法重新排列数对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        int n = pairs.size();
        unordered_map<int, int> cnt;
        unordered_map<int, vector<int>> g;
        for (int idx = 0; idx < n; ++idx) {
            int u = pairs[idx][0], v = pairs[idx][1];
            cnt[u] += 1;
            cnt[v] -= 1;
            g[u].push_back(idx);
        }
        int st = pairs[0][0];
        for (auto &[x, v] : cnt) {
            if (v == 1) {
                st = x;
                break;
            }
        }
        vector<int> path;
        vector<bool> used(n);
        auto dfs = [&](auto &&dfs, int u) -> void {
            while (g[u].size()) {
                int idx = g[u].back();
                int v = pairs[idx][1];
                g[u].pop_back();
                if (used[idx]) continue;
                used[idx] = true;
                dfs(dfs, v);
            }
            path.push_back(u);
        };
        dfs(dfs, st);
        reverse(path.begin(), path.end());
        vector<vector<int>> ans;
        for (int i = 1; i < path.size(); ++i) {
            ans.push_back({path[i - 1], path[i]});
        }
        return ans;
    }
};
// @lc code=end


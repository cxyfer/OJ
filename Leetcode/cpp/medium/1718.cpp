/*
 * @lc app=leetcode.cn id=1718 lang=cpp
 *
 * [1718] 构建字典序最大的可行序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        int m = 2 * n - 1;
        vector<int> ans(m, -1);
        vector<bool> vis(n + 1, false);
        auto dfs = [&](auto &&dfs, int i) -> bool {
            if (i == m) return true;
            if (ans[i] != -1) return dfs(dfs, i + 1);
            for (int x = n; x >= 1; x--) {
                if (vis[x]) continue;
                if (x == 1) {
                    ans[i] = 1;
                    vis[1] = true;
                    if (dfs(dfs, i + 1)) return true;
                    ans[i] = -1;
                    vis[1] = false;
                } else {
                    if (i + x < m && ans[i + x] == -1) {
                        ans[i] = ans[i + x] = x;
                        vis[x] = true;
                        if (dfs(dfs, i + 1)) return true;
                        ans[i] = ans[i + x] = -1;
                        vis[x] = false;
                    }
                }
            }
            return false;
        };
        dfs(dfs, 0);
        return ans;
    }
};
// @lc code=end


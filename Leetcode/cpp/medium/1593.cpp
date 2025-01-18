/*
 * @lc app=leetcode.cn id=1593 lang=cpp
 *
 * [1593] 拆分字符串使唯一子字符串的数目最大
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxUniqueSplit(string s) {
        int n = s.size();
        unordered_set<string> path;
        auto dfs = [&](auto &&dfs, int i) -> int {
            if (i == n) {
                return path.size();
            }
            int res = 0;
            for (int j = i + 1; j <= n; j++) {
                string sub_s = s.substr(i, j - i);
                if (path.find(sub_s) == path.end()) {
                    path.insert(sub_s);
                    res = max(res, dfs(dfs, j));
                    path.erase(sub_s);
                }
            }
            return res;
        };
        return dfs(dfs, 0);
    }
};
// @lc code=end
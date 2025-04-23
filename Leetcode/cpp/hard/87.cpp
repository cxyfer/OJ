/*
 * @lc app=leetcode.cn id=87 lang=cpp
 * @lcpr version=30204
 *
 * [87] 扰乱字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    unordered_map<string, bool> memo;
    bool dfs(const string &x, const string &y) {
        string key = x + "#" + y;
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;
        if (x == y) return memo[key] = true;

        string sx = x, sy = y;
        sort(sx.begin(), sx.end());
        sort(sy.begin(), sy.end());
        if (sx != sy) return memo[key] = false;

        int n = x.size();
        for (int i = 1; i < n; ++i) {
            if (dfs(x.substr(0, i), y.substr(0, i)) && dfs(x.substr(i), y.substr(i)))
                return memo[key] = true;
            if (dfs(x.substr(0, i), y.substr(n - i)) && dfs(x.substr(i), y.substr(0, n - i)))
                return memo[key] = true;
        }
        return memo[key] = false;
    };

    bool isScramble(string s1, string s2) {
        return dfs(s1, s2);
    }
};
// @lc code=end



/*
// @lcpr case=start
// "great"\n"rgeat"\n
// @lcpr case=end

// @lcpr case=start
// "abcde"\n"caebd"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n"a"\n
// @lcpr case=end

 */


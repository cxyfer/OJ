/*
 * @lc app=leetcode.cn id=93 lang=cpp
 * @lcpr version=30204
 *
 * [93] 复原 IP 地址
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        int n = s.size();
        vector<string> ans, path;
        auto dfs = [&](this auto &&dfs, int i) -> void {
            if (i == n) {
                if (path.size() == 4) {
                    string ip;
                    for (auto &&p : path)
                        ip += p + ".";
                    ip.pop_back();
                    ans.push_back(ip);
                }
                return;
            }
            if (path.size() == 4)
                return;
            if (s[i] == '0') {
                path.push_back(s.substr(i, 1));
                dfs(i + 1);
                path.pop_back();
                return;
            }
            for (int j = i; j < n; ++j) {
                if (stoi(s.substr(i, j - i + 1)) > 255)
                    break;
                path.push_back(s.substr(i, j - i + 1));
                dfs(j + 1);
                path.pop_back();
            }
            return;
        };
        dfs(0);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "25525511135"\n
// @lcpr case=end

// @lcpr case=start
// "0000"\n
// @lcpr case=end

// @lcpr case=start
// "101023"\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=2606 lang=cpp
 *
 * [2606] 找到最大开销的子字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        // return solve1(s, chars, vals);
        return solve2(s, chars, vals);
    }
    int solve1(string s, string chars, vector<int>& vals) {
        int n = s.size(), ans = 0;
        vector<int> mp(26, 0);
        for (int i = 0; i < 26; i++) mp[i] = i + 1;
        for (int i = 0; i < chars.size(); i++) mp[chars[i] - 'a'] = vals[i];
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            dp[i] = max(dp[i - 1] + mp[s[i - 1] - 'a'], mp[s[i - 1] - 'a']);
            ans = max(ans, dp[i]);
        }
        return ans;
    }
    int solve2(string s, string chars, vector<int>& vals) {
        int n = s.size(), ans = 0, f = 0;
        vector<int> mp(26, 0);
        for (int i = 0; i < 26; i++) mp[i] = i + 1;
        for (int i = 0; i < chars.size(); i++) mp[chars[i] - 'a'] = vals[i];
        for (char ch: s){
            f = max(f + mp[ch - 'a'], mp[ch - 'a']);
            ans = max(ans, f);
        }
        return ans;
    }
};
// @lc code=end


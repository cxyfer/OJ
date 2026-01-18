/*
 * @lc app=leetcode.cn id=1081 lang=cpp
 *
 * [1081] 不同字符的最小子序列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string smallestSubsequence(string s) {
        string ans = "";
        vector<int> cnt(26, 0);
        vector<bool> selected(26, false);
        for (char ch : s) cnt[ch - 'a']++;
        for (char ch : s) {
            if (!selected[ch-'a']) {
                while (!ans.empty() && ans.back() > ch && cnt[ans.back() - 'a'] > 0) {
                    selected[ans.back() - 'a'] = false;
                    ans.pop_back();
                }
                ans += ch;
                selected[ch - 'a'] = true;
            }
            cnt[ch - 'a']--;
        }
        return ans;
    }
};
// @lc code=end


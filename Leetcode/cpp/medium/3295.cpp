/*
 * @lc app=leetcode.cn id=3295 lang=cpp
 *
 * [3295] 举报垃圾信息
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) {
        int cnt = 0;
        unordered_set<string> bans(bannedWords.begin(), bannedWords.end());
        for (const string& word : message) {
            if (bans.count(word)) {
                cnt++;
                if (cnt >= 2) {
                    return true;
                }
            }
        }
        return false;
    }
};
// @lc code=end


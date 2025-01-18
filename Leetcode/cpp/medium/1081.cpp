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
    /*
        Greedy + Stack
        Similar to 402. Remove K Digits
        Same as 316. Remove Duplicate Letters
    */
    string smallestSubsequence(string s) {
        string ans = ""; // 用 String 來模擬 Stack
        int cnt[26] = {0};
        bool selected[26] = {false};
        for (char ch : s) cnt[ch - 'a']++;
        for (char ch : s) {
            if (!selected[ch-'a']) {
                // 這個字母比前面(Stack頂端)的字母小，且前面的字母還有剩餘，就把前面的字母刪掉(反悔)
                while (!ans.empty() && ans.back() > ch && cnt[ans.back()-'a'] > 0) {
                    selected[ans.back()-'a'] = false;
                    ans.pop_back();
                }
                ans += ch;
                selected[ch-'a'] = true;
            }
            cnt[ch-'a']--; // 使用一個 ch ，將其數量減一
        }
        return ans;
    }
};
// @lc code=end


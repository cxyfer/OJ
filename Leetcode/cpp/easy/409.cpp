/*
 * @lc app=leetcode.cn id=409 lang=cpp
 *
 * [409] 最长回文串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int longestPalindrome(string s) {
        int cnt[52] = {0};
        for (char ch: s){
            if ('a' <= ch && ch <= 'z') cnt[ch-'a']++;
            else cnt[ch-'A'+26]++;
        }
        int ans = 0, flag = 0;
        for (int i=0; i<52; ++i){
            ans += cnt[i] >> 1;
            if (cnt[i] & 1) flag = 1;
        }
        return (ans << 1) + flag;
    }
};
// @lc code=end


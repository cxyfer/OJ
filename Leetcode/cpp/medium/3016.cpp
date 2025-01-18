/*
 * @lc app=leetcode.cn id=3016 lang=cpp
 *
 * [3016] 输入单词需要的最少按键次数 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumPushes(string word) {
        vector<int> cnt(26, 0);
        for (char ch : word) cnt[ch - 'a']++;
        sort(cnt.begin(), cnt.end(), greater<int>());
        int ans = 0;
        for (int i = 0; i < 26; i++) ans += cnt[i] * (i / 8 + 1);
        return ans;
    }
};
// @lc code=end
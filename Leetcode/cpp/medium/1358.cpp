/*
 * @lc app=leetcode.cn id=1358 lang=cpp
 *
 * [1358] 包含所有三种字符的子字符串数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int ans = 0, left = 0, have = 0;
        vector<int> cnt(3);
        for (char ch : s) {
            cnt[ch - 'a'] += 1;
            if (cnt[ch - 'a'] == 1) {
                have += 1;
            }
            while (have == 3) {
                cnt[s[left] - 'a'] -= 1;
                if (cnt[s[left] - 'a'] == 0) {
                    have -= 1;
                }
                left += 1;
            }
            ans += left;
        }
        return ans;
    }
};
// @lc code=end


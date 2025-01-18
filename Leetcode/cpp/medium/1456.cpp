/*
 * @lc app=leetcode.cn id=1456 lang=cpp
 *
 * [1456] 定长子串中元音的最大数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxVowels(string s, int k) {
        int n = s.size();
        int ans = 0, have = 0;
        for (int r = 0; r < n; r++) {
            if (isVowel(s[r])) have++;
            if (r < k - 1) continue;
            ans = max(ans, have);
            if (isVowel(s[r - k + 1])) have--;
        }
        return ans;
    }

    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
};
// @lc code=end


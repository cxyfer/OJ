/*
 * @lc app=leetcode.cn id=1163 lang=cpp
 * @lcpr version=30204
 *
 * [1163] 按字典序排在最后的子串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string lastSubstring(string s) {
        int n = s.size();
        int i = 0, j = 1;
        while (j < n) {
            int ln = 0;
            while (j + ln < n && s[j + ln] == s[i + ln]) ln++;
            if (j + ln < n && s[j + ln] > s[i + ln]) {
                int nxt = max(j + 1, i + ln + 1);
                i = j;
                j = nxt;
            } else {
                j = j + ln + 1;
            }
        }
        return s.substr(i);
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abab"\n
// @lcpr case=end

// @lcpr case=start
// "leetcode"\n
// @lcpr case=end

 */


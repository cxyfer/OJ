/*
 * @lc app=leetcode.cn id=1392 lang=cpp
 * @lcpr version=30204
 *
 * [1392] 最长快乐前缀
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string longestPrefix(string s) {
        int n = s.size();
        vector<int> pi(n);
        int ln = 0;
        for (int i = 1; i < n; ++i) {
            while (ln && s[i] != s[ln]) ln = pi[ln - 1];
            if (s[i] == s[ln]) ln++;
            pi[i] = ln;
        }
        return s.substr(0, pi[n - 1]);
    }
};
// @lc code=end



/*
// @lcpr case=start
// "level"\n
// @lcpr case=end

// @lcpr case=start
// "ababab"\n
// @lcpr case=end

 */


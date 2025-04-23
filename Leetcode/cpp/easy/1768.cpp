/*
 * @lc app=leetcode.cn id=1768 lang=cpp
 * @lcpr version=30204
 *
 * [1768] Merge Strings Alternately
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int ln = min(word1.size(), word2.size());
        string ans;
        for (int i = 0; i < ln; i++)
            ans += word1.substr(i, 1) + word2.substr(i, 1);
        ans += word1.substr(ln) + word2.substr(ln);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abc"\n"pqr"\n
// @lcpr case=end

// @lcpr case=start
// "ab"\n"pqrs"\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n"pq"\n
// @lcpr case=end

 */


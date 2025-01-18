/*
 * @lc app=leetcode id=2000 lang=cpp
 * @lcpr version=30122
 *
 * [2000] Reverse Prefix of Word
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string reversePrefix(string word, char ch) {
        int idx = word.find(ch);
        if (idx != -1) reverse(word.begin(), word.begin() + idx + 1);
        return word;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abcdefd"\n"d"\n
// @lcpr case=end

// @lcpr case=start
// "xyxzxe"\n"z"\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n"z"\n
// @lcpr case=end

 */


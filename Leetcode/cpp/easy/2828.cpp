/*
 * @lc app=leetcode id=2828 lang=cpp
 * @lcpr version=30112
 *
 * [2828] Check if a String Is an Acronym of Words
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        if (words.size() != s.size()) return false;
        for (int i = 0; i < words.size(); i++) {
            if (words[i][0] != s[i]) return false;
        }
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["alice","bob","charlie"]\n"abc"\n
// @lcpr case=end

// @lcpr case=start
// ["an","apple"]\n"a"\n
// @lcpr case=end

// @lcpr case=start
// ["never","gonna","give","up","on","you"]\n"ngguoy"\n
// @lcpr case=end

 */


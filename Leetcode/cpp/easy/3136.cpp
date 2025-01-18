/*
 * @lc app=leetcode id=3136 lang=cpp
 * @lcpr version=30201
 *
 * [3136] Valid Word
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isValid(string word) {
        if (word.size() < 3) return false;
        bool ck1 = false, ck2 = false;
        for (char ch : word) {
            if (isalpha(ch)) {
                ch = tolower(ch);
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') ck1 = true;
                else ck2 = true;
            } else if (!isdigit(ch)) {
                return false;
            }
        }
        return ck1 && ck2;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "234Adas"\n
// @lcpr case=end

// @lcpr case=start
// "b3"\n
// @lcpr case=end

// @lcpr case=start
// "a3$e"\n
// @lcpr case=end

 */


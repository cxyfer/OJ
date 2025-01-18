/*
 * @lc app=leetcode id=2942 lang=cpp
 * @lcpr version=30112
 *
 * [2942] Find Words Containing Character
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;
        for (int i = 0; i < words.size(); i++) {
            if (words[i].find(x) != string::npos) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["leet","code"]\n"e"\n
// @lcpr case=end

// @lcpr case=start
// ["abc","bcd","aaaa","cbc"]\n"a"\n
// @lcpr case=end

// @lcpr case=start
// ["abc","bcd","aaaa","cbc"]\n"z"\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode id=709 lang=cpp
 * @lcpr version=30112
 *
 * [709] To Lower Case
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string toLowerCase(string s) {
        string ans = s;
        for (int i=0; i<s.size(); i++){
            if (s[i] >= 'A' && s[i] <= 'Z')
                ans[i] = s[i] - 'A' + 'a';
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "Hello"\n
// @lcpr case=end

// @lcpr case=start
// "here"\n
// @lcpr case=end

// @lcpr case=start
// "LOVELY"\n
// @lcpr case=end

 */


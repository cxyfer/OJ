/*
 * @lc app=leetcode id=2390 lang=cpp
 * @lcpr version=30122
 *
 * [2390] Removing Stars From a String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string removeStars(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '*') {
                if (!st.empty()) st.pop();
            } else {
                st.push(c);
            }
        }
        string ans;
        while (!st.empty()) {
            ans.push_back(st.top()); st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "leet**cod*e"\n
// @lcpr case=end

// @lcpr case=start
// "erase*****"\n
// @lcpr case=end

 */


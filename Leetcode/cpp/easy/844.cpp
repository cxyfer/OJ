/*
 * @lc app=leetcode id=844 lang=cpp
 * @lcpr version=30122
 *
 * [844] Backspace String Compare
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return build(s) == build(t);
    }
    string build(string s) {
        stack<char> st;
        for (char ch : s) {
            if (ch == '#') {
                if (!st.empty()) st.pop();
            } else {
                st.push(ch);
            }
        }
        string ans;
        while (!st.empty()) {
            ans.push_back(st.top());
            st.pop();
        }
        // reverse(ans.begin(), ans.end()); // 其實不需要反轉
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "ab#c"\n"ad#c"\n
// @lcpr case=end

// @lcpr case=start
// "ab##"\n"c#d#"\n
// @lcpr case=end

// @lcpr case=start
// "a#c"\n"b"\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=678 lang=cpp
 * @lcpr version=30204
 *
 * [678] Valid Parenthesis String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool checkValidString(string s) {
        int n = s.size();
        stack<int> st, st_s;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                st.push(i);
            } else if (s[i] == ')') {
                if (!st.empty()) st.pop();
                else if (!st_s.empty()) st_s.pop();
                else return false;
            } else {
                st_s.push(i);
            }
        }
        if (st.size() > st_s.size()) return false;
        while (!st.empty() && !st_s.empty()) {
            if (st.top() > st_s.top()) return false;
            st.pop();  st_s.pop();
        }
        return true;
    }
};

class Solution2 {
public:
    bool checkValidString(string s) {
        int mn = 0, mx = 0;
        for (char ch : s) {
            if (ch == '(') {
                mn++;
                mx++;
            } else if (ch == ')') {
                mn = max(0, mn - 1);
                mx--;
                if (mx < 0) return false;
            } else {
                mn = max(0, mn - 1);
                mx++;
            }
        }
        return mn == 0;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "()"\n
// @lcpr case=end

// @lcpr case=start
// "(*)"\n
// @lcpr case=end

// @lcpr case=start
// "(*))"\n
// @lcpr case=end

 */


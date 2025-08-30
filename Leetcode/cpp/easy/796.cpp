/*
 * @lc app=leetcode.cn id=796 lang=cpp
 * @lcpr version=30204
 *
 * [796] 旋转字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool rotateString(string s, string goal) {
        int n = s.size(), m = goal.size();
        if (n != m) return false;
        s += s;
        vector<int> pi(m);
        int ln = 0;
        for (int i = 1; i < m; ++i) {
            while (ln && s[i] != s[ln]) ln = pi[ln - 1];
            if (s[i] == s[ln]) ln++;
            pi[i] = ln;
        }
        ln = 0;
        for (int i = 0; i < 2 * n; ++i) {
            while (ln && s[i] != goal[ln]) ln = pi[ln - 1];
            if (s[i] == goal[ln]) ln++;
            if (ln == m) return true;
        }
        return false;
    }
};

class Solution2 {
public:
    bool rotateString(string s, string t) {
        int n = s.size(), m = t.size();
        if (n != m) return false;
        s = t + "#" + s + s;
        n = s.size();
        vector<int> pi(n);
        int ln = 0;
        for (int i = 1; i < n; ++i) {
            while (ln && s[i] != s[ln]) ln = pi[ln - 1];
            if (s[i] == s[ln]) ln++;
            if (ln == m) return true;
            pi[i] = ln;
        }
        return false;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "abcde"\n"cdeab"\n
// @lcpr case=end

// @lcpr case=start
// "abcde"\n"abced"\n
// @lcpr case=end

 */


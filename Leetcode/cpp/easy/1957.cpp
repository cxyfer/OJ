/*
 * @lc app=leetcode.cn id=1957 lang=cpp
 * @lcpr version=30204
 *
 * [1957] 删除字符使字符串变好
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    string makeFancyString(string s) {
        int n = s.size();
        string ans;
        for (int i = 0; i < n; ) {
            int j = i;
            for (; j < n && s[j] == s[i]; j++);
            ans += string(min(2, j - i), s[i]);
            i = j;
        }
        return ans;
    }
};

class Solution2 {
public:
    string makeFancyString(string s) {
        int n = s.size();
        string ans;
        for (int i = 0; i < n; i++)
            if (i < 2 || s[i] != s[i - 1] || s[i] != s[i - 2])
                ans += s[i];
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "leeetcode"\n
// @lcpr case=end

// @lcpr case=start
// "aaabaaaa"\n
// @lcpr case=end

// @lcpr case=start
// "aab"\n
// @lcpr case=end

 */


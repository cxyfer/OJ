/*
 * @lc app=leetcode.cn id=3403 lang=cpp
 * @lcpr version=30204
 *
 * [3403] 从盒子中找出字典序最大的字符串 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string answerString(string s, int k) {
        if (k == 1) return s;
        int n = s.size(), ln = n - k + 1;
        string ans = "";
        for (int i = 0; i < n; i++)
            ans = max(ans, s.substr(i, ln));
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "dbca"\n2\n
// @lcpr case=end

// @lcpr case=start
// "gggg"\n4\n
// @lcpr case=end

 */


/*
 * @lc app=leetcode.cn id=2138 lang=cpp
 * @lcpr version=30204
 *
 * [2138] 将字符串拆分为若干长度为 k 的组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int n = s.size();
        vector<string> ans;
        for (int i = 0; i < n; i += k)
            ans.push_back(s.substr(i, k));
        if (ans.back().size() < k)
            ans.back().append(k - ans.back().size(), fill);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abcdefghi"\n3\n"x"\n
// @lcpr case=end

// @lcpr case=start
// "abcdefghij"\n3\n"x"\n
// @lcpr case=end

 */


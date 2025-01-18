/*
 * @lc app=leetcode id=3110 lang=cpp
 * @lcpr version=30122
 *
 * [3110] Score of a String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int scoreOfString(string s) {
        int n = s.size(), ans = 0;
        for (int i = 1; i < n; i++)
            ans += abs(s[i] - s[i - 1]);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "hello"\n
// @lcpr case=end

// @lcpr case=start
// "zaz"\n
// @lcpr case=end

 */


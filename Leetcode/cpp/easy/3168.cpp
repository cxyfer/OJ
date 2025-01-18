/*
 * @lc app=leetcode.cn id=3168 lang=cpp
 *
 * [3168] 候诊室中的最少椅子数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumChairs(string s) {
        int ans = 0, cur = 0;
        for (char ch : s) {
            if (ch == 'E') ans = max(ans, ++cur);
            else cur--;
        }
        return ans;
    }
};
// @lc code=end


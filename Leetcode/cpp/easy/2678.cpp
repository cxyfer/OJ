/*
 * @lc app=leetcode.cn id=2678 lang=cpp
 *
 * [2678] 老人的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countSeniors(vector<string>& details) {
        int ans = 0;
        for (string& detail : details)
            if ((detail[11] - '0') * 10 + (detail[12] - '0') > 60)
                ans++;
        return ans;
    }
};
// @lc code=end


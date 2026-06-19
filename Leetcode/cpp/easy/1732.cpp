/*
 * @lc app=leetcode id=1732 lang=cpp
 *
 * [1732] Find the Highest Altitude
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0, s = 0;
        for (auto& x : gain) {
            s += x;
            ans = max(ans, s);
        }
        return ans;
    }
};
// @lc code=end


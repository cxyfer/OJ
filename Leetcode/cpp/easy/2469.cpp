/*
 * @lc app=leetcode id=2469 lang=cpp
 * @lcpr version=30111
 *
 * [2469] Convert the Temperature
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> ans;
        ans.push_back(celsius + 273.15);
        ans.push_back(celsius * 1.80 + 32.00);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 36.50\n
// @lcpr case=end

// @lcpr case=start
// 122.11\n
// @lcpr case=end

 */


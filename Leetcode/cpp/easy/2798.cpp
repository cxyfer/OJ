/*
 * @lc app=leetcode id=2798 lang=cpp
 * @lcpr version=30122
 *
 * [2798] Number of Employees Who Met the Target
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int ans = 0;
        for (int h : hours) ans += (h >= target);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [0,1,2,3,4]\n2\n
// @lcpr case=end

// @lcpr case=start
// [5,1,4,2,2]\n6\n
// @lcpr case=end

 */


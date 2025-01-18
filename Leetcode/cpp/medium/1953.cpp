/*
 * @lc app=leetcode.cn id=1953 lang=cpp
 *
 * [1953] 你可以工作的最大周数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        int mx = *max_element(milestones.begin(), milestones.end());
        LL s = accumulate(milestones.begin(), milestones.end(), 0LL);
        return (mx > s - mx + 1) ? (s - mx) << 1 | 1 : s;
    }
};
// @lc code=end


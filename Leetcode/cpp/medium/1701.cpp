/*
 * @lc app=leetcode.cn id=1701 lang=cpp
 *
 * [1701] 平均等待时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        int n = customers.size();
        double tot = 0;
        int cur = 0;
        for (auto& c : customers) {
            cur = max(cur, c[0]) + c[1];
            tot += cur - c[0];
        }
        return tot / n;
    }
};
// @lc code=end

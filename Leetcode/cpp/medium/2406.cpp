/*
 * @lc app=leetcode.cn id=2406 lang=cpp
 *
 * [2406] 将区间分为最少组数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        priority_queue<int, vector<int>, greater<int>> hp; // Min Heap
        for (const auto& interval : intervals) {
            if (!hp.empty() && hp.top() < interval[0]) {
                hp.pop();
            }
            hp.push(interval[1]);
        }
        return hp.size();
    }
};
// @lc code=end


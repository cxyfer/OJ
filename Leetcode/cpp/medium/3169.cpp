/*
 * @lc app=leetcode.cn id=3169 lang=cpp
 *
 * [3169] 无需开会的工作日
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        vector<pair<int, int>> res;
        for (int i = 0; i < meetings.size(); i++) {
            int x = meetings[i][0], y = meetings[i][1];
            if (res.empty() || res.back().second < x) {
                res.push_back({x, y});
            } else {
                res.back().second = max(res.back().second, y);
            }
        }
        int ans = days;
        for (auto& p : res) {
            ans -= p.second - p.first + 1;
        }
        return ans;
    }
};
// @lc code=end


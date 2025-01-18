/*
 * @lc app=leetcode.cn id=452 lang=cpp
 *
 * [452] 用最少数量的箭引爆气球
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int ans = 1, right = points[0][1];
        for (auto& p : points) {
            if (p[0] > right) {
                right = p[1];
                ans++;
            }
        }
        return ans;
    }
};
// @lc code=end

// @lcpr case=start
// [[-2147483648,2147483647]]\n
// @lcpr case=end


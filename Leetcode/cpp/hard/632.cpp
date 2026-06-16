/*
 * @lc app=leetcode.cn id=632 lang=cpp
 *
 * [632] 最小区间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int INF = 0x3f3f3f3f;
class Solution1 {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int n = nums.size();
        int left = -INF, right = INF;  // answer
        int mx = -INF;                 // initial max value
        for (int i = 0; i < n; i++) mx = max(mx, nums[i][0]);
        // Min heap, (value, row, col)
        priority_queue<array<int, 3>, vector<array<int, 3>>,
                       greater<array<int, 3>>>
            pq;
        for (int i = 0; i < n; i++) pq.push({nums[i][0], i, 0});
        while (true) {
            auto [mn, i, j] = pq.top();  // pop min value
            pq.pop();
            if (mx - mn < right - left) {  // update answer
                left = mn, right = mx;
            }
            if (j == nums[i].size() - 1) break;
            mx = max(mx, nums[i][j + 1]);         // update max value
            pq.push({nums[i][j + 1], i, j + 1});  // push next value
        }
        return {left, right};
    }
};

using Solution = Solution1;
// @lc code=end


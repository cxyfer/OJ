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
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        return solve1(nums);
    }
    vector<int> solve1(vector<vector<int>>& nums) {
        int n = nums.size();
        int left = -INF, right = INF; // answer
        int mx = -INF; // initial max value
        for (int i = 0; i < n; i++) mx = max(mx, nums[i][0]);
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq; // Min heap, (value, row, col)
        for (int i = 0; i < n; i++) pq.push({nums[i][0], i, 0});
        while (true) {
            auto t = pq.top(); pq.pop();
            int mn = get<0>(t), i = get<1>(t), j = get<2>(t); // pop min value
            if (mx - mn < right - left) { // update answer
                left = mn, right = mx;
            }
            if (j == nums[i].size() - 1) break;
            mx = max(mx, nums[i][j + 1]); // update max value
            pq.push({nums[i][j + 1], i, j + 1}); // push next value
        }
        return {left, right};
    }
};
// @lc code=end


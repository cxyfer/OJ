/*
 * @lc app=leetcode.cn id=699 lang=cpp
 *
 * [699] 掉落的方块
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        int n = positions.size();
        vector<int> h(n, 0);
        for (int i = 0; i < n; i++) {
            int left = positions[i][0];
            int length = positions[i][1];
            int right = left + length - 1;
            h[i] = length;
            for (int j = 0; j < i; j++) {
                int left2 = positions[j][0];
                int right2 = positions[j][0] + positions[j][1] - 1;
                if (right >= left2 && left <= right2) {
                    h[i] = max(h[i], h[j] + length);
                }
            }
        }
        // 將 h 更新為放置第 i 個方塊後的最高高度，注意最高高度可能比第 i 個方塊的高度高
        for (int i = 1; i < n; i++) {
            h[i] = max(h[i], h[i - 1]);
        }
        return h;   
    }
};
// @lc code=end
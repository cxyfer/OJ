/*
 * @lc app=leetcode.cn id=3047 lang=cpp
 * @lcpr version=30204
 *
 * [3047] 求交集区域内的最大正方形面积
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int n = bottomLeft.size();
        int max_w = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int bx = max(bottomLeft[i][0], bottomLeft[j][0]);
                int by = max(bottomLeft[i][1], bottomLeft[j][1]);
                int tx = min(topRight[i][0], topRight[j][0]);
                int ty = min(topRight[i][1], topRight[j][1]);
                max_w = max(max_w, min(tx - bx, ty - by));
            }
        }
        return 1LL * max_w * max_w;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,1],[2,2],[3,1]]\n[[3,3],[4,4],[6,6]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1],[2,2],[1,2]]\n[[3,3],[4,4],[3,4]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1],[3,3],[3,1]]\n[[2,2],[4,4],[4,2]]\n
// @lcpr case=end

 */


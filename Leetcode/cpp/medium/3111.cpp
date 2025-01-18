/*
 * @lc app=leetcode id=3111 lang=cpp
 * @lcpr version=30122
 *
 * [3111] Minimum Rectangles to Cover Points
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#define INF 0x3f3f3f3f
class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
        int n = points.size();
        int ans = 0;
        int last = -INF;
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[0] < b[0];
        });
        for (auto p : points) {
            if (p[0] > last) {
                ans++;
                last = p[0] + w;
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[2,3],[1,2]]\n0\n
// @lcpr case=end

 */


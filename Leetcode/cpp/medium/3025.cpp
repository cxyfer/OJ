/*
 * @lc app=leetcode.cn id=3025 lang=cpp
 * @lcpr version=30204
 *
 * [3025] 人员站位的方案数 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 0;
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] > b[0] || (a[0] == b[0] && a[1] < b[1]);
        });
        for (int i = 0; i < n; i++) {
            int y1 = points[i][1];
            int min_y = INT_MAX;
            for (int j = i + 1; j < n; j++) {
                int y2 = points[j][1];
                if (y2 < y1) continue;
                if (min_y > y2) {
                    min_y = y2;
                    ans++;
                }
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,1],[2,2],[3,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[6,2],[4,4],[2,6]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,1],[1,3],[1,1]]\n
// @lcpr case=end

 */


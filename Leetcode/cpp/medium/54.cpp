/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
    const vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();

        vector<int> ans(m * n, -1);
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        int x = 0, y = 0, nx, ny;
        int cd = 0; // current direction
        for (int i = 0; i < m * n; ++i){
            ans[i] = matrix[x][y];
            vis[x][y] = true;
            nx = x + dirs[cd][0]; ny = y + dirs[cd][1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny]) {
                cd = (cd + 1) % 4;
                nx = x + dirs[cd][0]; ny = y + dirs[cd][1];
            }
            x = nx, y = ny;
        }
        return ans;
    }
};
// @lc code=end


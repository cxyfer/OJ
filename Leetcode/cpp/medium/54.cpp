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
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> ans(m * n, -1);
        int x = 0, y = 0, nx, ny;
        int cd = 0; // current direction
        int DIRX[4]= {0, 1, 0, -1}, DIRY[4] = {1, 0, -1, 0};
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i = 0; i < m * n; ++i){
            ans[i] = matrix[x][y];
            visited[x][y] = true;
            nx = x + DIRX[cd]; ny = y + DIRY[cd];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || visited[nx][ny]) {
                cd = (cd + 1) % 4;
                nx = x + DIRX[cd]; ny = y + DIRY[cd];
            }
            x = nx, y = ny;
        }
        return ans;
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=994 lang=cpp
 *
 * [994] 腐烂的橘子
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        BFS
    */
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int DIRX[4] = {1, -1, 0, 0}, DIRY[4] = {0, 0, 1, -1};  
        queue<vector<int>> q;
        for (int i = 0; i < m; i++) 
            for (int j = 0; j < n; j++) 
                if (grid[i][j] == 2) 
                    q.push({i, j, 0});
        int ans = 0;
        while (!q.empty()){
            auto cur = q.front(); q.pop();
            int x = cur[0], y = cur[1], t = cur[2];
            ans = t;
            for (int k = 0; k < 4; k++) {
                int nx = x + DIRX[k], ny = y + DIRY[k];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == 1){
                    grid[nx][ny] = 2;
                    q.push({nx, ny, t+1});
                }
            }
        }
        for (int i = 0; i < m; i++) 
            for (int j = 0; j < n; j++) 
                if (grid[i][j] == 1) return -1;
        return ans;
    }
};
// @lc code=end


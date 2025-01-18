/*
 * @lc app=leetcode.cn id=1958 lang=cpp
 *
 * [1958] 检查操作是否合法
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
        function<bool(int, int)> check = [&](int dx, int dy) {
            int x = rMove + dx, y = cMove + dy;
            int cnt = 0;
            while (0 <= x && x < 8 && 0 <= y && y < 8) {
                if (board[x][y] == color) return cnt > 0;
                if (board[x][y] == '.') return false;
                x += dx;
                y += dy;
                cnt++;
            }
            return false;
        };
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (dx == 0 && dy == 0) continue;
                if (check(dx, dy)) return true;
            }
        }
        return false;
    }
};
// @lc code=end

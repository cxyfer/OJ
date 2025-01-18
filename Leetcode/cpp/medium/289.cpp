/*
 * @lc app=leetcode.cn id=289 lang=cpp
 *
 * [289] 生命游戏
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*  
        使用額外狀態，但是不使用額外空間
        用最後2bit表示當前狀態和下一時刻狀態，最低位表示當前狀態，倒數第二位表示下一時刻狀態
        而 0 為死， 1 為活，故 00 表示死，01 表示活變死，10 表示死變活，11 表示活
        由於第二位初始就是 0 ，所以只要判斷下一時刻狀態為活的情況即可
    */
    void gameOfLife(vector<vector<int>>& board) {
        int r = board.size(), c = board[0].size();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int live = 0; // 計算周圍活細胞數
                for (int x = i - 1; x <= i + 1; x++) {
                    for (int y = j - 1; y <= j + 1; y++) {
                        if (x >= 0 && x < r && y >= 0 && y < c && (x != i || y != j)) {
                            live += board[x][y] & 1;
                        }
                    }
                }
                if (board[i][j] & 1) { // 活細胞保持活
                    board[i][j] += (live == 2 || live == 3) << 1;
                } else { // 死細胞變活
                    board[i][j] += (live == 3) << 1;
                }
            }
        }
        for (int i = 0; i < r; i++) { // 更新狀態
            for (int j = 0; j < c; j++) {
                board[i][j] >>= 1;
            }
        }
    }
};
// @lc code=end


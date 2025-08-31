/*
 * @lc app=leetcode.cn id=37 lang=cpp
 *
 * [37] 解数独
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<int> row(9), col(9), box(9);
        auto set = [&](int i, int j, int val) -> void {
            row[i] |= (1 << val);
            col[j] |= (1 << val);
            box[i / 3 * 3 + j / 3] |= (1 << val);
        };
        auto unset = [&](int i, int j, int val) -> void {
            row[i] &= ~(1 << val);
            col[j] &= ~(1 << val);
            box[i / 3 * 3 + j / 3] &= ~(1 << val);
        };
        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j)
                if (board[i][j] != '.') set(i, j, board[i][j] - '1');

        auto dfs = [&](this auto&& dfs, int i, int j) -> bool {
            if (i == 9) return true;
            if (j == 9) return dfs(i + 1, 0);
            if (board[i][j] != '.') return dfs(i, j + 1);
            // for (int k = 0; k < 9; ++k) {
            //     if (row[i] & (1 << k) || col[j] & (1 << k) || box[i / 3 * 3 + j / 3] & (1 << k)) continue;
            for (int msk = (row[i] | col[j] | box[i / 3 * 3 + j / 3]) ^ ((1 << 9) - 1); msk; msk &= (msk - 1)) {
                int k = bit_width(static_cast<unsigned>(msk & -msk)) - 1;
                set(i, j, k);
                board[i][j] = '1' + k;
                if (dfs(i, j + 1)) return true;
                unset(i, j, k);
                board[i][j] = '.';
            }
            return false;
        };
        dfs(0, 0);
        return;
    }
};
// @lc code=end

